from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status, HTTPException

from .. import models
from ..hashing import PasswordHash


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def register_user(db: Session, username, email, password):
    pass_hash_obj = PasswordHash(password)
    hashed_password = pass_hash_obj.hashed_password
    new_user = models.User(username=username, email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_request_id(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'The user is not found with the user {id} id')
    return user
