from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status, HTTPException

from .. import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_user(db: Session, title, body):
    new_blog = models.Blog(title=title, body=body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blog(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'The blog is not found with thi blog {id} id')
    return blog


def update_blog(id, request, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'The blog is not found with thi blog {id} id')
    blog.update(dict(request))
    db.commit()

    message = {'message': f'blog associate with id {id} is updated sucessfully'}

    return message


def delete_blog(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'The blog is not found with thi blog {id} id')

    blog.delete(synchronize_session=False)
    db.commit()

    message = {'message': f'blog associate with id {id} is deleted sucessfully'}

    return message
