from fastapi import FastAPI, HTTPException
from uuid import uuid4
from models import User
app = FastAPI()


users = [
    {"id":uuid4(),"username":"vishal","email":"vishalpatil@gmail.com"},
    {"id":uuid4(),"username":"vivek","email":"vivekjha@gmail.com"},
]

@app.get("/",tags=["ROOT"])
def root():
    return {"Ping":"Pong"}

@app.get("/users",tags=["GET_ALL_USERS"])
def get_all():
    return users


@app.post("/users",tags=["CREATE_USER"])
def create_user(user:User):
    user.id = uuid4()
    users.append(user.dict())
    return {"data":"user create successfully"}


@app.get("/users/{id}",tags=["GET_USER_BY_ID"])
def get_user_by_id(id:str):
    for user in users:
        if str(user["id"]) == id:
            return user
    raise HTTPException(404,"user not found")


@app.put("/users/{id}",tags=["UPDATE_USER"])
def update_user(id:str,userdata:User):
    for user in users:
        if str(user["id"]) == id:
            user['username'] = userdata.username
            user["email"] = userdata.email
            return user
    raise HTTPException(404,"user not found")


@app.delete("/users/{id}",tags=["DELETE_USER"])
def delete_user(id:str):
    for user in users:
        if str(user['id']) == id:
            users.remove(user)
            return {"data":"user removed successfully"}
    raise HTTPException(404,"user not found")