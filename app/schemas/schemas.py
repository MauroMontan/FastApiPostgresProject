from pydantic import BaseModel


class ShowUserSchema(BaseModel):
    email:str

    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    email:str
    password: str




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email:str
