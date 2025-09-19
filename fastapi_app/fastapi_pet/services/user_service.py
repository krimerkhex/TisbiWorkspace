from sqlalchemy.orm import Session
from fastapi_pet.models.user import User
from fastapi_pet.schemas.user_schema import UserCreate


class UserCRUD:

    @classmethod
    def get_user_by_email(cls, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()

    @classmethod
    def get_user_by_login(cls, db: Session, login: str) -> User:
        return db.query(User).filter(User.login == login).first()

    @classmethod
    def create_user(cls, db: Session, user: UserCreate) -> User:
        db_user = User(
            login=user.login,
            email=user.email,
            password=user.password  # храним пароль в открытом виде
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @classmethod
    def get_users(cls, db: Session, skip: int = 0, limit: int = 100) -> list[User]:
        return db.query(User).offset(skip).limit(limit).all()

    @classmethod
    def get_user_by_id(cls, db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()

    @classmethod
    def update_user(cls, db: Session, user_id: int, user_data: dict) -> User:
        db_user = cls.get_user_by_id(db, user_id)
        if db_user:
            for key, value in user_data.items():
                if hasattr(db_user, key):
                    setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        return db_user

    @classmethod
    def delete_user(cls, db: Session, user_id: int) -> bool:
        db_user = cls.get_user_by_id(db, user_id)
        if db_user:
            db.delete(db_user)
            db.commit()
            return True
        return False

    @classmethod
    def verify_user_credentials(cls, db: Session, login: str, password: str) -> bool:
        """Проверка учетных данных пользователя"""
        user = cls.get_user_by_login(db, login)
        if user and user.password == password:  # прямое сравнение паролей
            return True
        return False