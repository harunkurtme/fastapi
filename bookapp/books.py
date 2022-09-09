from typing import Optional
from unittest import skip
from fastapi import FastAPI
from enum import Enum

app=FastAPI()


BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}

@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_favorite_book():
        return {"my_favorite_book":"My favorite Book"}

@app.get("/books/{book_title}")
async def read_book(book_title):
    return {"book_title":book_title}


@app.get("/books/{book_id}")
async def read_book_id(book_id:int): #book_id must be int
    return {"book_title":book_id}


class DirectionName(str,Enum): #Enum Model
    north="North"
    south="Sout"
    east="East"
    west="West"

@app.get("/diretions/{direction_name}")
async def get_direction(direction_name:DirectionName): #must_Be directionName clas
    if direction_name==DirectionName.north:
        return {"Direciton":direction_name,"sub":"Up"}
    if direction_name==DirectionName.north:
        return {"Direciton":direction_name,"sub":"Down"}
    if direction_name==DirectionName.west:
        return {"Direciton":direction_name,"sub":"Left"}
    if direction_name==DirectionName.east:
        return {"Direciton":direction_name,"sub":"Right"}


@app.get("/{book_name}")
async def read_book(book_name:str):
    return BOOKS[book_name]

@app.get("/{book_name}")
async def skip_book(skip_book:str="book_3"): 
    new_books=BOOKS.copy()
    del new_books[skip_book]
    return new_books

# this function optinal call from books
#if you add a string value from boooks 
# and operating to delete
@app.get("/{book_name}")
async def optinalCallBook(skip_book:Optional[str]=None):
    if skip_book: 
        new_books=BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

@app.post("/")
async def create_book(book_title,book_author):
    current_book_id=0
    if len(BOOKS)>0:
        for book in BOOKS:
            x= int(book.split('_')[-1])
            if x>current_book_id:
                current_book_id=x
                
    BOOKS[f'book_{current_book_id+1}']={'title':book_title,'author':book_author}
    
    return BOOKS[f'book_{current_book_id+1}']