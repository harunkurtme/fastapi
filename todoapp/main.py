from fastapi import FastAPI, Depends
import models
from database import engine,sessionlocal
from sqlalchemy.orm import Session

app=FastAPI()

models.base.metadata.create_all(engine) # creeate todos.sql

def get_db():
    try:
        db= sessionlocal()
        yield db
    finally:
        db.close()


#depends at get_db value with yield 
#regular value
@app.get("/")
async def create_database(db:Session=Depends(get_db)):
    return db.query(models.Todos).all()


@app.get