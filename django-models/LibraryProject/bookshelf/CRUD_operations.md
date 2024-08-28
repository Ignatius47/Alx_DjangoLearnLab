### Create Operation

from bookshelf.models import Book
book1 = Book.objects.create(title = "Scream", author = "James Bond", publication_year = 2020)
# Successfully created a book instance and saved it to the database.

### from retrieve_md document
>>> from bookshelf.models import Book
>>> retrieve_book = Book.objects.get(title = "Scream")
>>> print(retrieve_book)
# Expected outcome : [<Book: Scream by James Bond year 2020>]>


### from update.md document
>>> book_update = Book.objects.get(title = "Scream")
>>> book_update.title = "Scream"
>>> book_update.save()

# Expected outcome 
>>> print(retrieve_book)
 # [<Book: Scream by James Bond year 2020>]>

 
### from delete_md 
>>> from bookshelf.models import Book
>>> delete_book = Book.objects.get(title = "Scream")
>>> delete_book.delete()
(1, {'bookshelf.Book': 1})

# Expected outcome 
 # print(retrieve_book)
  # <[]> no book present

