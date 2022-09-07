from unicodedata import name
from sqlalchemy.orm import Session

from typing import Optional

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, hashed_password=user.password, name=user.name)
    db.add(db_user)
    db.commit() 
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.UserUpdate, current_user: models.User):
    db_user: models.User = get_user(db, current_user.id)
    db_user.username = user.username if user.username is not None else db_user.username
    db_user.name = user.name if user.name is not None else db_user.name
    db_user.hashed_password = user.password if user.password is not None else db_user.hashed_password
    db.commit()

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    db.delete(db_user)
    db.commit()
