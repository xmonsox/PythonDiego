from fastapi import FastAPI, Depends
#invocamos esa session
from db.session import get_session
from sqlalchemy.orm import Session
from models.users import User


#Libreria para validar datos, poderosisisisisima
from pydantic import BaseModel
#crear onjeto de fastapi
app = FastAPI()



@app.post("/test")
async def test_db(db: Session = Depends(get_session)):
    result = db.query(User).all()
    return {"result": result}
    

#valida los tipos
class Numero(BaseModel):
    num:int
#decorador
@app.get("/")
async def index():
    return {"Message " : "Hello World"}

@app.post("/suma")
async def get_suma(num1:int, num2:int):
    return {"Resultado" : num1+num2}

# def validarDato(dato):
#     try:
#         tipoDato = int(dato)
#     except ValueError:
#         return {"Message " : "El dato que indico no es entero"}

@app.post("/numero")
async def validar_numero(numero:Numero):
    if (numero.num>0 and numero.num<100):
        if (numero.num% 2 == 0):
            fact = 1
            for i in range(numero.num):
                fact = fact * (i+1)
            division = numero.num/2
            return {
                        "Message " : "El numero es par",
                        "Factorial " : fact,
                        "Division" : division
                    }
        else: 
            fact = 1
            for i in range(numero.num):
                fact = fact * (i+1)
            division = numero.num/2
            return {
                        "Message " : "El numero es impar",
                        "Factorial " : fact,
                        "Division" : division
                    }
    else:
        return {"Message " : "EL numero no esta entre los permitidos"}




 