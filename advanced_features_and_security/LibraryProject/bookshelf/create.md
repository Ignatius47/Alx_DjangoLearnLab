from bookshelf.models import Book
book1 = Book.objects.create(title = "Scream", author = "James Bond", publication_year = 2020)
# Successfully created a book instance and saved it to the database.