from fastapi import FastAPI
from models import Book, Author

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Welcome to the library!"}

@app.get("/books/")
async def get_books():
    return {"message": "Here is your book list"}

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return {"book_id": book_id}                             ##get database book id

@app.post("/books/")
async def create_book(book: Book):    ##create book on database
    book_dict = book.dict()

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book): ##update database book
    pass

@app.delete("/books/{book_id}")
async def delete_book(book_id: int): ##delete database book
    pass 



@app.get("/authors")
async def get_authors():
    return {"message": "here would be your author list"}

