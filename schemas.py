from typing import List, Union

from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    description: str
    career: str
    characters: str
    img: str
    tree_id: int


class PersonCreate(PersonBase):
    pass


class PersonRead(PersonBase):
    id: int


class RelationBase(BaseModel):
    person1_id: int
    person2_id: int
    status: str


class RelationCreate(RelationBase):
    pass


class RelationRead(RelationBase):
    id: int


class TreeBase(BaseModel):
    name: str
    description: str
    img: str
    token: str
    bg_img: str


class TreeCreate(TreeBase):
    user_id: int

    class Config:
        orm_mode = True


class TreeRead(TreeBase):
    id: int
    persons: List[PersonRead] = []


class UserBase(BaseModel):
    login: str
    email: str
    status: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    hashed_password: str
    trees: List[TreeRead] = []

    class Config:
        orm_mode = True


class UserAccess(BaseModel):
    login: str
    password: str

class Token(BaseModel):
    user: str
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

    class Config:
        orm_mode = True
