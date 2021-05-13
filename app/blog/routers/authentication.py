from sqlalchemy.orm.session import Session
from blog import database
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from blog import schemas, database, models
from blog.hashing import Hash
from blog.token import create_access_token
from sqlalchemy.orm import Session
from datetime import timedelta
router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Crediential')

    if not Hash().verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Crediential')

    # Genrate a jwt token and return
    access_token = create_access_token(data={"sub": user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}
