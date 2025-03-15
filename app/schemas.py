from pydantic import BaseModel


# Schema for creating a new Todo (does NOT require an id)
class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool


# Schema for returning a Todo (includes id)
class Todo(TodoCreate):
    id: int


class UserCreate(BaseModel):
    name: str
    password: str


class User(UserCreate):
    id: int
