from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])
user_database = Database(User)

@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким логином уже есть"
        )
    await user.create()
    return {"message": "Пользователь зарегистрирован"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователя с таким логином не существует"
        )
    if user_exist.password == user.password:
        return {"message": "Пользователь вошел в систему"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Некорректные данные"
    )
