from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session, select
import json
from database.connection import get_session
from models.users import User, UserCreate, UserSignIn

user_router = APIRouter(tags=["User"])

@user_router.post("/signup")
async def sign_new_user(data: UserCreate, session: Session = Depends(get_session)):
    # Проверяем, нет ли пользователя с таким email
    existing_user = session.exec(select(User).where(User.email == data.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="ПОЛЬЗОВАТЕЛЬ С ТАКИМ ЛОГИНОМ УЖЕ СУЩЕСТВУЕТ"
        )
    
    # Конвертируем events в JSON строку
    user_data = data.dict()
    user_data['events'] = json.dumps(data.events)
    
    user = User(**user_data)
    session.add(user)
    session.commit()
    
    return {"message": "ПОЛЬЗОВАТЕЛЬ ЗАРЕГИСТРИРОВАН"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.email == user.email)).first()
    
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ПОЛЬЗОВАТЕЛЯ НЕ СУЩЕСТВУЕТ"
        )
    
    if db_user.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="НЕВЕРНЫЙ ПАРОЛЬ"
        )
    
    return {"message": "ПОЛЬЗОВАТЕЛЬ ВОШЕЛ УСПЕШНО"}