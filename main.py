from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#Fast api routes parameters line by line so if we need to static routing just above the dynamic routing

#if we want additional parametrs as optional
@app.get('/blogs')
def index(limit = 10, published:bool= True, sort:Optional[str] =None):
    if published:
        return {'data': f'{limit} published blogs in the db'}
    else:
        return {'data': f'{limit} blogs in the db'}


@app.get('/blog/unpublished')
def uppublished_blog():
    return {'data': "unpublished_blog"}


@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1, 2'}}


class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def create_blog(request:Blog):
    return {'data': f'blog is created with {request.title}'}