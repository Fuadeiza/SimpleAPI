from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role
from typing import List

app = FastAPI()


db: List[User] = [
    User(id=uuid4(), first_name= "Jamila", last_name= "Ahmed", gender=Gender.female, roles=[Role.user]),
    User(id=uuid4(), first_name= "Alex", last_name= "Jones", gender=Gender.male, roles = [Role.admin]),
    User(id=uuid4(), first_name= "Jane", last_name= "Doe", gender=Gender.male, roles=[Role.user])

]

@app.get("/")
def root():
    return {"Hello": "Fast"}


@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}