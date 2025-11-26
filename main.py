from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "ESTE ES EL ARCHIVO CORRECTO"}


from pydantic import BaseModel

class Datos(BaseModel):
    a: float
    b: float

@app.post("/sumar")
def sumar(datos: Datos):
    resultado = datos.a + datos.b
    return {"resultado": resultado}
