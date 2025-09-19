from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    login: str
    email: str  # EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    login: str
    email: str

    class Config:
        from_attributes = True
