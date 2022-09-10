from http.client import HTTPException
from pyexpat import model
from fastapi import FastAPI, Depends,HTTPException
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


@app.get("/todo/{todo_id}")
async def read_todo(todo_id:int,db:Session=Depends(get_db)):
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    raise http_exception()

def http_exception():
    return HTTPException(status_code=404,detail="Todo not found")