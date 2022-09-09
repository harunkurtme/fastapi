from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID

"""
_summary_
get/ all boks
get/ book uuid
put / book uuid
post / create new book
delete / book uuid specific book

we create BASEMODEL with class
"""

class Book(BaseModel):
    id: UUID
    title:str = Field(min_length=1) #must be one character for title
    author: str 
    description:str
    rating:int
    

app =FastAPI()
BOOKS=[]

@app.get("/")
async def read_all_books():
    return BOOKS


@app.post('/')
async def create_book(book:Book):
    BOOKS.append(book)
    return book