from fastapi import FastAPI
from app.routes.todo_routes import router
from app.routes.user_routes import router as auth_router
from app.routes.url_shortener_routes import router as url_shortener_router

app = FastAPI()

app.include_router(router)
app.include_router(auth_router)
app.include_router(url_shortener_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
