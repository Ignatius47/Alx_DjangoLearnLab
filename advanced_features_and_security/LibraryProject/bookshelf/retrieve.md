>>> from bookshelf.models import Book
>>> retrieve_book = Book.objects.get(title = "Scream")
>>> print(retrieve_book)
# Expected outcome : [<Book: Scream by James Bond year 2020>]>

