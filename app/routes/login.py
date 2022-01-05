from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..security.hashing import Hash
from ..database.database import get_db
from ..models.models import UserModel
from ..security.token import create_access_token

router = APIRouter(prefix="/login", tags=["login"])


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session= Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your are not signed")
    

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="incorrect password")
    

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
