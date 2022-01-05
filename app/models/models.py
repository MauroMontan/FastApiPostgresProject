from sqlalchemy import String,Column,Integer
import sqlalchemy.orm as orm
from ..database.database import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


