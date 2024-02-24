from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username": "testuser",
                "email":"test@gmail.com",
                "password":"Test12345",
                "is_staff":False,
                "is_active": True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str = '2fcc9b863b6caa36fad83dff54fe23c13eff78730560085c0b731a100f85d919'


class LoginModel(BaseModel):
    username:str
    password:str
