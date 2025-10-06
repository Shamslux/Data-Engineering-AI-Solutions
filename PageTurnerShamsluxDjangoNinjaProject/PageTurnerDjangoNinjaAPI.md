![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) 
![Django Ninja](https://img.shields.io/badge/Django%20Ninja-000000?style=for-the-badge&logo=django&logoColor=yellow) 
![ChatGPT](https://img.shields.io/badge/ChatGPT-000000?style=for-the-badge&logo=openai&logoColor=white) 
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) 
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white) 
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-green?style=for-the-badge)
![Goodreads](https://img.shields.io/badge/Goodreads-372213?style=for-the-badge&logo=goodreads&logoColor=white)

# Project Purpose

This was a project built with Python + Django + Django Ninja that originated from an internal request at my current company. My technical lead asked the developers to create a **fictional study project**, since we would soon be responsible for maintaining and developing a product that uses the same technology stack.

We had about **two business days**, using roughly **1 hour of our workday**, to create a deliverable that would later be analyzed and used for feedback to improve our software development processes.

> Note: I really enjoyed this proposal, as I didn’t come from a programming background — I was inserted directly into the Data field without prior experience as a software developer. I’ve always liked programming as a hobby, and this exercise helped me learn more about API creation, database integration, and related topics.

# Key Points

- This project was **for study purposes** and built under a **very limited timeframe**, so it’s not refined with best practices beyond what was feasible within the time given.  
- I chose to use the fictional company **PageTurner** (which uses data extracted from the Goodreads dataset) because I’m already using that same dataset in another ongoing project where I’m studying **Microsoft Fabric** (which I plan to publish soon).  
- The **frontend** was built quickly as well — I didn’t focus on refining certain aspects (e.g., too many elements on the pages, minimal custom CSS). I also used **TailwindCSS via CDN**. I haven’t formally studied this framework (as I did with Bootstrap before), but I liked its appearance and decided to stick with it, assisted by generative AI.

# Basic Usability

![main_page_view](https://github.com/user-attachments/assets/4b945efb-571b-47ca-bfdb-071f5b8da397)

The image above shows the **home page** and basic navigation buttons. The goal is to present the fictional company with its open API for public access to the book catalog. In the Microsoft Fabric project, there’s also a sales catalog, but this one is truly public since it exposes the list of books available in the Goodreads dataset.

![system_view](https://github.com/user-attachments/assets/cb022a1e-263e-4ead-8a3f-35e5f8a376bb)

The image above shows the **system screen** and the possible tests for our endpoints. Below is the code used to create our basic CRUD:

```python
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
```

## Searching for Books

![search](https://github.com/user-attachments/assets/3f1857cb-ca41-4df4-b6b1-a00e13892f5e)

This is the page that allows us to use the API to **query books** in the public catalog. We can toggle the filter by title, author, or ID, or leave it on automatic (the search bar will try to identify the entered value automatically).

![filter](https://github.com/user-attachments/assets/6fbbdd68-6e1e-4b1b-918f-5dfe4543eef1)

## Creating / Registering a Book in the Catalog

![create](https://github.com/user-attachments/assets/54b6976c-a3c9-4708-a692-afa7b9e2b31e)

We can create a new book in the catalog, as shown in the image above. After entering the correct information (there are a few basic validations), a success message will appear (image below):

![created](https://github.com/user-attachments/assets/4955b82b-8c44-4505-b5a8-9615d609e99e)

## Updating a Record

![new_book](https://github.com/user-attachments/assets/1460cfed-2590-48f6-8356-492bcec366c7)

We created the `0000` ID when the insertion succeeded, adding a new record to the book catalog. I kept everything very generic. Let’s say we now want to update the title from `A title` to something else.

![update](https://github.com/user-attachments/assets/8dc254a7-8c71-4fe3-a9ef-5402cdd3f62f)

As we can see, everything worked correctly, and we received a success message.

![updated](https://github.com/user-attachments/assets/94ef67ea-ee2d-489c-82be-f9292f5b8e55)

> Note: I had to quickly adjust the code because it originally blocked the use of a zero ID. For this test, I used `id = 0`, although I could have retrieved the latest created ID. Still, that wouldn’t be ideal since it’s not easy to find it via the site. The correct approach would be to let the database handle ID generation automatically. But as mentioned, this was a very rudimentary educational project.

## Deleting a Record

![delete](https://github.com/user-attachments/assets/55ef0a69-8d89-4696-a935-757e4a7a5423)

Now we can delete our test record using the delete option.

![really](https://github.com/user-attachments/assets/b1d09538-579e-48ca-84d6-f182a82c566c)

We’ll receive a warning to confirm that we truly wish to delete the record.

![deleted](https://github.com/user-attachments/assets/adda0415-1337-425d-81b8-253ed6bf913f)

We’ll then receive a confirmation message that the record was deleted.

![no_exists](https://github.com/user-attachments/assets/f6f5e0a6-67de-41a6-b9f5-8d757da3ce2c)

If we check afterward, we’ll see that there’s no longer any result for the old record `0000`.

# Conclusion

This is a **simple and educational project**, but it was a fun adventure to learn how to use **Django + Django Ninja** to create a robust API for the **PageTurner** system.  

Thank you for taking the time to read through it!  

The project includes **Docker configuration**, so feel free to download and run it locally, make improvements, and continue studying beyond where I left off.













