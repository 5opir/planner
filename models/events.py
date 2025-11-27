from sqlmodel import SQLModel, Field, Column
from typing import Optional, List
import json

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: str  # Будем хранить как JSON строку
    location: str
    class Config:
        schema_extra = {
            "example": {
                "title": "Презентация книги FastAPI",
                "image": "https://cdn.prod.website-files.com/65e6d3081f98733f1b369f14/66067e35b34ea0fbb0ab1602_fastapi-framwork-logo.png",
                "description": "Будем что-то обсуждать",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
        
class EventCreate(SQLModel):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    class Config:
        schema_extra = {
            "example": {
                "title": "Презентация книги FastAPI",
                "image": "https://cdn.prod.website-files.com/65e6d3081f98733f1b369f14/66067e35b34ea0fbb0ab1602_fastapi-framwork-logo.png",
                "description": "Будем что-то обсуждать",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "title": "Презентация книги FastAPI",
                "image": "https://cdn.prod.website-files.com/65e6d3081f98733f1b369f14/66067e35b34ea0fbb0ab1602_fastapi-framwork-logo.png",
                "description": "Будем что-то обсуждать",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }