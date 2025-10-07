from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from fastapi_pet.utils.helpers import get_db
from fastapi_pet.schemas.user_schema import UserCreate, UserResponse
from fastapi_pet.services.user_service import UserCRUD
from fastapi_pet.models.user import User

user_router = APIRouter()


@user_router.post("/api/register/", response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserCRUD.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")

    db_user = UserCRUD.get_user_by_login(db, login=user.login)
    if db_user:
        raise HTTPException(status_code=400, detail="Логин уже занят")

    return UserCRUD.create_user(db=db, user=user)


@user_router.get("/api/users/", response_model=list[UserResponse])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = UserCRUD.get_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/api/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user
