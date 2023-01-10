from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    age : int
    name : str
    etc : Optional[bool] = None

@app.get("/")
def read_root():
    return {"hi" : "hello"}

@app.get("/user/{user_id}")
def read_item(user_id : int, name: Optional[str] = None) :
    return {"user_id" : user_id, "name" : name}

@app.put("/user/{user_id}")
def update_user(user_id : int, user : User):
    return {"user_id" : user_id, "user_name" : user.name}