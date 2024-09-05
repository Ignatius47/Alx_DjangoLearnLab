from django.db import models

# Model to represent an author
class Author(models.Model):
    # Field for the author's name, limited to a maximum of 100 characters
    name = models.CharField(max_length=100)

    # String representation of the author object, which will display the author's name
    def __str__(self):
        return self.name


# Model to represent a book
class Book(models.Model):
    # Field for the book's title, limited to a maximum of 200 characters
    title = models.CharField(max_length=200)
    
    # Field for the book's publication year, stored as an integer
    publication_year = models.IntegerField()
    
    # Foreign key field linking the book to an author
    # When the author is deleted, all related books are also deleted (CASCADE)
    # 'related_name' specifies how this relationship will be accessed from the Author model
    # In this case, 'books' will allow reverse lookup of books authored by a specific author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    # String representation of the book object, which will display the book's title
    def __str__(self):
        return self.title
