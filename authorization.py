from calendar import timegm
from datetime import datetime
from datetime import timedelta

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials, HTTPBearer
import jwt
from werkzeug.security import check_password_hash

from db.database import Session, get_db
from settings import settings_loader
from schemas import *
from db.models import User

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

security = HTTPBearer()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        user_session = jwt.decode(token, settings_loader('SECRET_KEY'), algorithms=settings_loader('ALGORITHM'))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Session invalid")


def verify_password(plain_password, hashed_password):
    return check_password_hash(hashed_password, plain_password)


def authenticate_user(password: str, user):
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = timegm(datetime.utcnow().utctimetuple()) + \
             timedelta(hours=settings_loader('ACCESS_TOKEN_EXPIRE_HOURS')).total_seconds()

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings_loader('SECRET_KEY'), algorithm=settings_loader('ALGORITHM'))
    return encoded_jwt


@router.post("/")
def login_for_access_token(
        form_data: UserAccess = Depends(), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.login == form_data.login).first()
    is_granted = authenticate_user(form_data.password, user)
    if not is_granted:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user": user.login})
    return Token(user=user.login, access_token=access_token, token_type='Bearer')
