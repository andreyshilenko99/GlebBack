from typing import List

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from db import Base
from db import TimeStampMixin


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    status = Column(String, nullable=False)
    tree = relationship("Tree", back_populates="user")


class Tree(Base):
    __tablename__ = 'trees'

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(String)
    img = Column(String)
    bg_img = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="tree")
    person = relationship("Person", back_populates="tree")


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    career = Column(String)
    characters = Column(String)
    img = Column(String)
    tree_id = Column(Integer, ForeignKey('trees.id'))
    tree = relationship("Tree", back_populates="person")


class Relation(Base):
    __tablename__ = 'relations'

    id = Column(Integer, primary_key=True, index=True)
    person1_id = Column(Integer)
    person2_id = Column(Integer)
    status = Column(String)
