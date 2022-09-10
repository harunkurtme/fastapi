from fastapi import FastAPI
import models
from database import engine

app=FastAPI()

models.base.metadata.create_all(engine) # creeate todos.sql

@app.get("/")
async def create_database():
    return {"Database":"Created"}
