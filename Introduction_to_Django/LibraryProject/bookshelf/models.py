from django.db import models
# Create your models here.
 
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length = 100),
    publication_year = models.IntegerField()





    from bookshelf.models import Book


new_book = Book.objects.create(
    title="Diving into Backend", 
    author="jake tapper", 
   
    publication_year="2026-02-25",
)
print(f"Book '{new_book.title}' created with ID: {new_book.id}")