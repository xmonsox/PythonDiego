from fastapi import FastAPI
#Libreria para validar datos, poderosisisisisima
from pydantic import BaseModel, StringConstraints
# Unir tipo de dato con adiciones 
from typing import Annotated

app = FastAPI()

class UserData(BaseModel):
    name: Annotated[str, StringConstraints(max_length=40)] #solo para string
    status: bool
    age: int

class UserPassword(UserData):
    password: Annotated[str, StringConstraints(max_length=100)] #solo para string


@app.post("/UserData")
async def showData(data:UserData):
    return {
                "Message " : "Correct",
                "UserName " : data.name,
                "UserAge " : data.age,
                "UserStatus " : data.status,
            }

@app.get("/getUserData")
async def getUser():
    return {
                "Message " : "Correct",
                "UserName " : "data",
                "UserAge " : "data",
                "UserStatus " : "data",
                "UserPassword " : "1234"
            }





