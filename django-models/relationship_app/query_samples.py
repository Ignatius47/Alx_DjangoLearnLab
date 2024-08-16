from relationship_app.models import Author, Book

author_name = "Jack Reacher"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author_name)

for book in books_by_author:
    print(book.title)

from relationship_app.models import Library, Book

library_name = "Michelin Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

for book in books_in_library:
    print(book.title)

from relationship_app.models import Librarian, Library

library_name = "Michelin Library"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)

print(librarian.name)
