from fastapi import APIRouter, HTTPException, status
from models.users import User, NewUser, UserSignIn

user_router = APIRouter(tags=["User"])
users = {}

@user_router.post("/signup")
async def sign_new_user(data: NewUser) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с указанным именем пользователя существует"
        )
    users[data.email] = data
    return {"message": "Пользователь успешно зарегистрировался!"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не существует"
        )
    
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Переданы неправильные учетные данные"
        )
    
    return {"message": "Пользователь успешно вошел в систему"}