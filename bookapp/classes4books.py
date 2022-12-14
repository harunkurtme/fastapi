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

app =FastAPI()
BOOKS=[]


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

def create_books_no_api():
    book_1 = Book(id="71f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=60)
    book_2 = Book(id="21f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=70)
    book_3 = Book(id="31f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=80)
    book_4 = Book(id="41f4c2ea-1340-41f4-89f7-2852347bb0d1",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=90)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)




@app.get("/")
async def read_all_books(books_to_return: Optional[int]=None):

    # this is book length not make 
    # maked a lots books
    if len(BOOKS)<1:
        create_books_no_api()
    
    
    if books_to_return and len(BOOKS)>=books_to_return >0:
        i =1
        new_books=[]
        while i <=books_to_return:
            new_books.append(BOOKS[i-1])
            i+=1
        return new_books
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id==book_id:
            return x

@app.post('/')
async def create_book(book:Book):
    BOOKS.append(book)
    return book

#changed with uuid 
#as book_id with update
@app.put("/{book_id}")
async def update_book(book_id:UUID,book:Book):
    counter =0
    for x in BOOKS:
        counter +=1
        if x.id==book_id:
            BOOKS[counter-1]=book
            return BOOKS[counter-1]

@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    counter =0
    for x in BOOKS:
        counter+=1
        if x.id==book_id:
            del BOOKS[counter-1]
            return f"id : {book_id} deleted."
        