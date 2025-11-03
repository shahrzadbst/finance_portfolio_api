# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        username=user.username,
        hashed_password=user.password  # Hash password in production!
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()
