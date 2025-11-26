from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from models.events import Event
from models.users import User
from pydantic import BaseModel
from typing import Any, List, Optional


# Класс Database для CRUD операций
class Database:
    def __init__(self, model):
        self.model = model