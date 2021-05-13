from typing import List
from fastapi import APIRouter
from blog import schemas, database, models
from blog.Oauth import get_current_user
from blog.repository.blog import get_all, create_user, get_blog, update_blog, delete_blog

from fastapi import FastAPI, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all_blog(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return create_user(db, request.title, request.body)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_particular_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return get_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return update_blog(id, request, db)


@router.delete('/{id}', status_code=200)
def destroy(id: int,  db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return delete_blog(id, db)
