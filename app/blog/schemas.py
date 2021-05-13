from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    email: str
    username: str
    password: str


class ShowUser(BaseModel):
    email: str
    username: str

    class Config():
        orm_mode = True


class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
