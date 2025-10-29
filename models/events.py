from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Презентация книги FastAPI",
                "image": "https://cdn.prod.website-files.com/65e6d3081f98733f1b369f14/66067e35b34ea0fbb0ab1602_fastapi-framwork-logo.png",
                "description": "Будем что-то обсуждать",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }