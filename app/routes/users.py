
from fastapi import APIRouter, Depends
from ..security.hashing import Hash
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..schemas.schemas import ShowUserSchema, UserSchema
from ..models.models import UserModel
from ..utils.db_utils import add_row


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=ShowUserSchema)
def register(request: UserSchema, db: Session = Depends(get_db)):
    newUser = UserModel(email=request.email,
                        password=Hash.bcrypt(request.password))


    add_row(newUser, db)

    return newUser


