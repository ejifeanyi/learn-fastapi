from fastapi import APIRouter
from app.schemas import User, UserCreate

router = APIRouter()


users = [
    User(id=1, name="James", password="password"),
    User(id=2, name="John", password="anotherPassword"),
]

