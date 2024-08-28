from django.shortcuts import render

# Create your views here.
from bookshelf.models import Book

delete_book = Book.objects.delete(title = "Nineteen Eighty-Four")
