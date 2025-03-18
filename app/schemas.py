from pydantic import BaseModel


# Schema for creating a new Todo (does NOT require an id)
class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool


# Schema for returning a Todo (includes id)
class Todo(TodoCreate):
    id: int


class User(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class Shorten_url(BaseModel):
    url: str

class Original_url(BaseModel):
    url: str
class Url(BaseModel):
    shorten_url: str
    original_url: str