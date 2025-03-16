from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.schemas import UserCreate, UserLogin, Token, User
from app.services.auth import hash_password, verify_password, create_access_token

router = APIRouter()

users_db = {}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/register", response_model=Token)
async def register_user(user: UserCreate):
    #   check if username exists in database
    #   hash password
    #   store access token from data username
    #   return access token

    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = hash_password(user.password)

    users_db[user.username] = hashed_password
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login_user(user: UserLogin):
    # check if username exists in database
    # return 404 not found error if user is not found
    # compare password with what was recieved
    # return access token if password if password is correct
    # return incorrect password if password is not correct

    if user.username not in users_db:
        raise HTTPException(status_code=404, detail="User does not exist!")

    hashed_password = users_db[user.username]
    compared_password = verify_password(user.password, hashed_password)
    if compared_password:
        access_token = create_access_token(data={"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect password!")


@router.get("/users/{username}", response_model=User)
def get_user(username: str):
    # find username from user_db
    # return user if found
    # else return user not found

    if username in users_db:
        password = users_db[username]
        return {"username": username, "password": password}

    raise HTTPException(status_code=404, detail="User does not exist!")
