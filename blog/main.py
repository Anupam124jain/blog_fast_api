from blog.routers import authentication
from fastapi import FastAPI

from . import models
from .routers import blog, user, authentication
from .database import engine


app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(engine)
