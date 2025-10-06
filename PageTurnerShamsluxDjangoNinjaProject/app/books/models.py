from django.db import models

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True, db_column="book_id")
    title = models.CharField(max_length=500)
    authors_raw = models.TextField()
    average_rating = models.FloatField(null=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    isbn13 = models.CharField(max_length=20, null=True, blank=True)
    language_code = models.CharField(max_length=10, null=True, blank=True)
    num_pages = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True)
    text_reviews_count = models.IntegerField(null=True)
    publication_date = models.DateField(null=True)
    publisher = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'books'
