from http.client import HTTPException
from pyexpat import model
from typing import Optional
from fastapi import FastAPI, Depends,HTTPException
import models
from database import engine,sessionlocal
from sqlalchemy.orm import Session
from pydantic import BaseModel,Field # for post

app=FastAPI()

models.base.metadata.create_all(engine) # creeate todos.sql

def get_db():
    try:
        db= sessionlocal()
        yield db
    finally:
        db.close()

class Todo(BaseModel):
    #post request
    title=str
    description=Optional[str]
    priority:int=Field(gt=0,lt=6,description="must be between 1-5")
    complete:bool

#depends at get_db value with yield 
#regular value
@app.get("/")
async def create_database(db:Session=Depends(get_db)):
    return db.query(models.Todos).all()

#read_todo function want todo_id from person
#and depend take it db also 
@app.get("/todo/{todo_id}")
async def read_todo(todo_id:int,db:Session=Depends(get_db)):
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    raise http_exception()

#post with we make new 
@app.post("/")
async def create_todo(todo:Todo,db:Session=Depends(get_db)):
    todo_model=models.Todos()
    todo_model.title=todo.title
    todo_model.description=todo.description
    todo_model.complete=todo.complete
    db.add(todo_model)
    db.commit()
    
    return{
        "status":201,
        "transaction":"Successful"
    }

@app.put("/{todo_id}")
async def update_todo(todo_id:int,todo:Todo,db:Session=Depends(get_db)):
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first()
    
    if todo_model is None:
        raise http_exception()
    
    todo_model.title=todo.title
    todo_model.description=todo.description
    todo_model.priority=todo.priority
    todo_model.complete= todo.complete
    
    db.add(todo_model)
    db.commit()
    
    return{
        "status":201,
        "transaction":"Successful"
    }
@app.delete("/{todo_id}}")
async def delete_todo(todo_id:int,db:Session=Depends(get_db))):
    todo_model=db.query(models.Todos).filter(models.Todos.id==todo_id).first
    if todo_model is None:
        raise http_exception()
    
    db.query(models.Todos.id).filter(models.Todos.id==todo_id).delete()
    db.commit()
    

def successful_response(status_code : int):
    
    return{
        "status":status_code,
        "transaction":"Successful"
    }
#http exception function
#if we take it mistake value from person 
#we showing with http_exception func
def http_exception():
    return HTTPException(status_code=404,detail="Todo not found")

