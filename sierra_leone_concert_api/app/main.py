from fastapi import FastAPI
from app.routers import (
    plays_routers,
    actors_routers,
    directors_routers,
    tickets_routers,
    customers_routers,
    showtimes_routers,
    auth_routers
)

app = FastAPI(title="Sierra Leone Concert Management API")

app.include_router(auth_routers.router)
app.include_router(plays_routers.router)
app.include_router(actors_routers.router)
app.include_router(directors_routers.router)
app.include_router(tickets_routers.router)
app.include_router(customers_routers.router)
app.include_router(showtimes_routers.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Concert Management API!"}
