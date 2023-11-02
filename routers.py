from typing import List

from fastapi import Depends, APIRouter, HTTPException
from werkzeug.security import generate_password_hash

from authorization import has_access
from db.database import Session, get_db
from db.models import Tree, Person, Relation, User
from schemas import UserRead, UserCreate, TreeRead, TreeCreate, PersonRead, PersonCreate, RelationRead, RelationCreate
from utils import generate_request_id

router = APIRouter(dependencies=[Depends(has_access)])


@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(login=user.login,
                   hashed_password=generate_password_hash(user.password),
                   email=user.email,
                   status=user.status)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user


@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in user.dict().items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user


@router.delete("/users/{user_id}", response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    db.close()
    return db_user


@router.post("/trees/", response_model=TreeRead)
def create_tree(tree: TreeCreate, db: Session = Depends(get_db)):
    tree.token = generate_request_id()
    db_tree = Tree(**tree.dict())
    db.add(db_tree)
    db.commit()
    db.refresh(db_tree)
    db.close()
    return db_tree


@router.get("/trees/{tree_id}", response_model=TreeRead)
def read_tree(tree_id: int, db: Session = Depends(get_db)):
    tree = db.query(Tree).filter(Tree.id == tree_id).first()
    db.close()
    if tree is None:
        raise HTTPException(status_code=404, detail="Tree not found")
    return tree


@router.put("/trees/{tree_id}", response_model=TreeRead)
def update_tree(tree_id: int, tree: TreeCreate, db: Session = Depends(get_db)):
    db_tree = db.query(Tree).filter(Tree.id == tree_id).first()
    if db_tree is None:
        db.close()
        raise HTTPException(status_code=404, detail="Tree not found")

    for field, value in tree.dict().items():
        setattr(db_tree, field, value)

    db.commit()
    db.refresh(db_tree)
    db.close()
    return db_tree


@router.delete("/trees/{tree_id}", response_model=TreeRead)
def delete_tree(tree_id: int, db: Session = Depends(get_db)):
    db_tree = db.query(Tree).filter(Tree.id == tree_id).first()
    if db_tree is None:
        db.close()
        raise HTTPException(status_code=404, detail="Tree not found")

    db.delete(db_tree)
    db.commit()
    db.close()
    return db_tree


@router.post("/persons/", response_model=PersonRead)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    db_person = Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    db.close()
    return db_person


@router.get("/persons/{person_id}", response_model=PersonRead)
def read_person(person_id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.id == person_id).first()
    db.close()
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@router.put("/persons/{person_id}", response_model=PersonRead)
def update_person(person_id: int, person: PersonCreate, db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if db_person is None:
        db.close()
        raise HTTPException(status_code=404, detail="Person not found")

    for field, value in person.dict().items():
        setattr(db_person, field, value)

    db.commit()
    db.refresh(db_person)
    db.close()
    return db_person


@router.delete("/persons/{person_id}", response_model=PersonRead)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if db_person is None:
        db.close()
        raise HTTPException(status_code=404, detail="Person not found")

    db.delete(db_person)
    db.commit()
    db.close()
    return db_person


@router.post("/relations/", response_model=RelationRead)
def create_relation(relation: RelationCreate, db: Session = Depends(get_db)):
    db_relation = Relation(**relation.dict())
    db.add(db_relation)
    db.commit()
    db.refresh(db_relation)
    db.close()
    return db_relation


@router.get("/relations/{relation_id}", response_model=RelationRead)
def read_relation(relation_id: int, db: Session = Depends(get_db)):
    relation = db.query(Relation).filter(Relation.id == relation_id).first()
    db.close()
    if relation is None:
        raise HTTPException(status_code=404, detail="Relation not found")
    return relation


@router.put("/relations/{relation_id}", response_model=RelationRead)
def update_relation(relation_id: int, relation: RelationCreate, db: Session = Depends(get_db)):
    db_relation = db.query(Relation).filter(Relation.id == relation_id).first()
    if db_relation is None:
        db.close()
        raise HTTPException(status_code=404, detail="Relation not found")

    for field, value in relation.dict().items():
        setattr(db_relation, field, value)

    db.commit()
    db.refresh(db_relation)
    db.close()
    return db_relation


@router.delete("/relations/{relation_id}", response_model=RelationRead)
def delete_relation(relation_id: int, db: Session = Depends(get_db)):
    db_relation = db.query(Relation).filter(Relation.id == relation_id).first()
    if db_relation is None:
        db.close()
        raise HTTPException(status_code=404, detail="Relation not found")

    db.delete(db_relation)
    db.commit()
    db.close()
    return db_relation



@router.get("/users/", response_model=List[UserRead])
def read_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    db.close()
    return users


@router.get("/trees/", response_model=List[TreeRead])
def read_all_trees(db: Session = Depends(get_db)):
    trees = db.query(Tree).all()
    db.close()
    return trees


@router.get("/persons/", response_model=List[PersonRead])
def read_all_persons(db: Session = Depends(get_db)):
    persons = db.query(Person).all()
    db.close()
    return persons


@router.get("/relations/", response_model=List[RelationRead])
def read_all_relations(db: Session = Depends(get_db)):
    relations = db.query(Relation).all()
    db.close()
    return relations