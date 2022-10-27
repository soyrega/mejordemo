from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"este es el equipo DTV"}


@app.get("/name/{name}")
def hello_name(name: str):
    return {"Hello": name}
