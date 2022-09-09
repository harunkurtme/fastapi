from fastapi import FastAPI

"""
_summary_
get/ all boks
get/ book uuid
put / book uuid
post / create new book
delete / book uuid specific book

we create BASEMODEL with class
"""

app =FastAPI()
BOOKS=[]

@app.get("/")
async def read_all_books():
    return BOOKS

