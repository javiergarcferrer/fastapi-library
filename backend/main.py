from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Welcome to the library!"}

@app.get("/books/")
async def get_books():
    return {"message": "Here is your book list"}

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    pass                             ##get database book id

@app.post("/books/{book_id}")
async def add_book(book_id: int):    ##add book to database
    pass

@app.put("/books/{book_id}")
async def update_book(book_id: int): ##update database book
    pass

@app.delete("/books/{book_id}")
async def delete_book(book_id: int): ##delete database book
    pass