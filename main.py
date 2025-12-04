from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.events import Event
from models.users import User
from routes.events import event_router
from routes.users import user_router

app = FastAPI()

# Инициализация базы данных при запуске
@app.on_event("startup")
async def on_startup():
    # Подключение к MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    
    # Инициализация Beanie
    await init_beanie(database=client.planner, document_models=[Event, User])

# Регистрация маршрутов
app.include_router(event_router, prefix="/event")
app.include_router(user_router, prefix="/user")

@app.get("/")
async def read_root():
    return {"message": "Здравствуйте, товарищ!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)