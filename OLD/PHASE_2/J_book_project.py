from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basics", "author": "John"},
    {"id": 2, "title": "FastAPI Guide", "author": "Alice"},
]

# Get all books
@app.get("/books")
def get_all_books():
    return books


# Get single book by title
@app.get("/books/{book_title}")
def get_book_by_title(book_title: str):
    for book in books:
        if book["title"].casefold() == book_title.casefold():
            return book

    raise HTTPException(status_code=404, detail="Book not found")


# Filter books by title (query parameter)
@app.get("/books/filter")
def filter_book_by_title(title: str):
    filtered = []

    for book in books:
        if book["title"].casefold() == title.casefold():
            filtered.append(book)

    return filtered


# Add new book
@app.post("/books")
def add_new(new_book: dict = Body()):
    books.append(new_book)

    return {
        "message": "New book added",
        "book": new_book
    }