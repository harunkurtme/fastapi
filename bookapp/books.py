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


class DirectionName(str,Enum):
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
    