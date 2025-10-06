from ninja import NinjaAPI, Router
from typing import List, Optional
from .models import Book
from django.shortcuts import get_object_or_404
from ninja.orm import create_schema
from django.db.models import Q

# Schemas for input and output
BookIn = create_schema(Book, name="BookIn", exclude=["created_at"])
BookOut = create_schema(
    Book,
    name="BookOut",
    fields=[
        "book_id", "title", "authors_raw", "average_rating",
        "isbn", "isbn13", "language_code", "num_pages",
        "ratings_count", "text_reviews_count", "publication_date",
        "publisher", "created_at"
    ]
)

book_router = Router(tags=["Books"])

# List books with optional search and mode filter
@book_router.get("/", response=List[BookOut])
def list_books(request, q: Optional[str] = None, mode: Optional[str] = "auto"):
    """
    List books. Supports optional search query `q` and filter mode:
    - auto (default): search title, authors, and ID
    - title: search only by title
    - author: search only by authors_raw
    - id: search by book_id only (exact match)
    """
    books = Book.objects.all()
    if q:
        q_clean = q.strip()
        mode = (mode or "auto").lower()

        if mode == "title":
            books = books.filter(title__icontains=q_clean)
        elif mode == "author":
            books = books.filter(authors_raw__icontains=q_clean)
        elif mode == "id":
            # Try to cast to int; if fails, return none
            try:
                books = books.filter(book_id=int(q_clean))
            except ValueError:
                books = books.none()
        else:  # auto
            books = books.filter(
                Q(title__icontains=q_clean) |
                Q(authors_raw__icontains=q_clean) |
                Q(book_id__icontains=q_clean)
            )
    return books

# Get book details by ID
@book_router.get("/{book_id}", response=BookOut)
def get_book(request, book_id: int):
    """Retrieve a single book by its book_id."""
    return get_object_or_404(Book, book_id=book_id)

# Create a new book
@book_router.post("/", response=BookOut)
def create_book(request, data: BookIn):
    """Create a new book record."""
    book = Book.objects.create(**data.dict())
    book.refresh_from_db()
    return book

# Update an existing book
@book_router.put("/{book_id}", response=BookOut)
def update_book(request, book_id: int, data: BookIn):
    """
    Update an existing book by book_id.
    The primary key (book_id) cannot be changed.
    """
    book = get_object_or_404(Book, book_id=book_id)
    for attr, value in data.dict().items():
        if attr == "book_id":  # do not allow changing the PK
            continue
        setattr(book, attr, value)
    book.save()
    book.refresh_from_db()
    return book

# Delete a book
@book_router.delete("/{book_id}", response={204: None})
def delete_book(request, book_id: int):
    """Delete a book by book_id."""
    book = get_object_or_404(Book, book_id=book_id)
    book.delete()
    return 204, None

# Main API object
api = NinjaAPI(
    title="PageTurner - API",
    version="1.0.0",
    description="API for managing books with endpoints for listing, creating, updating, and deleting."
)

# Add router with prefix "/books"
api.add_router("/books", book_router)
