from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID

from typing import Optional

"""
_summary_
get/ all boks
get/ book uuid
put / book uuid
post / create new book
delete / book uuid specific book

we create BASEMODEL with class
Optinal library null saffety with field

"""

class Book(BaseModel):
    id: UUID
    title:str = Field(min_length=1) #must be one character for title
    author: str 
    #optinal is use supply nullsaffety from typing library
    #dynamic validation thanks to optional library
    description:Optional[str]=Field(title="Description of the book", #field want to max lenth 100 
                          #min length 1
                          max_length=100,
                          min_length=1
                          )
    #rating is not greatdown and lastdown 102
    #must be rating at 0 and 100
    rating:int= Field(gt=-1,lt=101)
    
    #base model for description on the our api some information at
    #get, post or delete method
    class Config:
        schema_extra={
            "example":{
                "id":"uuid",
                "title":"for title",
                "author":"str",
                "description":"desc",
                "rating":75
                
            }
        }

app =FastAPI()
BOOKS=[]

@app.get("/")
async def read_all_books():
    return BOOKS


@app.post('/')
async def create_book(book:Book):
    BOOKS.append(book)
    return book