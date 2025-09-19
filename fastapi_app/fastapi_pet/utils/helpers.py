from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "sqlite")

if DB_TYPE == "postgres":
    # Настройки для PostgreSQL
    POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres_user")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres_password")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "postgres")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5430")

    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)

else:
    # Настройки для SQLite (по умолчанию)
    SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi_db.db"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_db_type():
    return DB_TYPE