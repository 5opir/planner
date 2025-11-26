from beanie import Document
from pydantic import EmailStr, Field
from typing import List, Optional
from pydantic import BaseModel

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[str]] = []

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "pass123"
            }
        }