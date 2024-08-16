>>> book = Book.objects.get(title = "Scream")
>>> book.title = "Scream"
>>> book.save()

# Expected outcome 
>>> print(retrieve_book)
 # [<Book: Scream by James Bond year 2020>]>