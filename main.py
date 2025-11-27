from fastapi import FastAPI
from database.connection import create_db_and_tables
from routes.events import event_router
from routes.users import user_router

app = FastAPI()

# Создаем таблицы при запуске
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Регистрируем маршруты
app.include_router(event_router, prefix="/event")
app.include_router(user_router, prefix="/user")

@app.get("/")
async def read_root():
    return {"message": "ЗДРАВСТВУЙТЕ, ТОВАРИЩ!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)