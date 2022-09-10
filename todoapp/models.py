from email.policy import default
from tkinter.tix import Tree
from sqlalchemy import Boolean,Column,Integer,String
from database import base

#model is show at todos model from database model
class Todos(base):
    __tablename__="todos"  #todo name
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    complete=Column(Boolean,default=False)
    
    