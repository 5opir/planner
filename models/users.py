from sqlmodel import SQLModel, Field
from typing import Optional, List
from pydantic import EmailStr

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    password: str
    events: Optional[str] = None 
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "pass123",
                "events": []
            }
        }

class UserCreate(SQLModel):
    email: EmailStr
    password: str
    events: Optional[List[str]] = []
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "pass123",
                "events": []
            }
        }

class UserSignIn(SQLModel):
    email: EmailStr
    password: str
