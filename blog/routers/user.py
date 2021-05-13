
from typing import List
from fastapi import APIRouter
from .. import schemas, database, models
from ..hashing import PasswordHash
from ..repository.user import register_user, get_user_request_id

from fastapi import FastAPI, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=['User']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return register_user(db, request.username, request.email, request.password)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_user(id: int,  db: Session = Depends(get_db)):
    return get_user_request_id(id, db)
