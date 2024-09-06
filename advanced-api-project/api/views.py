from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.exceptions import ValidationError
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework

# ListView to retrieve all Book records
class BookListView(generics.ListAPIView):
    """
    Retrieves the list of all books from the database.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Combine filtering, searching, and ordering into one filter_backends definition
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Define filter fields, search fields, and ordering fields
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']  # Assuming 'author' is a related model
    ordering_fields = ['title', 'publication_year']
    

# DetailView to retrieve a single Book by its ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by its 'id' (primary key).
    """
    queryset = Book.objects.all()  # Fetches all books, filtered by the lookup field
    serializer_class = BookSerializer  # Serializer to format the data
    lookup_field = 'id'  # Specifies that the lookup will be done via 'id'

# CreateView to handle adding a new Book with custom validation
class BookCreateView(generics.CreateAPIView):
    """
    Allows for the creation of a new book.
    Custom validation is added to ensure the 'publication_year' is not in the future.
    """
    queryset = Book.objects.all()  # Fetches all books
    serializer_class = BookSerializer  # Serializer for creating a new book

    def perform_create(self, serializer):
        """
        Custom method to handle validation before saving a new Book.
        Ensures the publication year is not in the future.
        """
        publication_year = serializer.validated_data.get('publication_year')  # Get the year from the request data
        current_year = datetime.now().year  # Get the current year
        if publication_year > current_year:
            raise ValidationError({'publication_year': 'The publication year cannot be in the future.'})  # Raise an error if year is in the future
        serializer.save()  # Save the book if validation passes

    def create(self, request, *args, **kwargs):
        """
        Custom response on successful book creation.
        """
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Book created successfully!',
            'book': response.data  # Include the created book data in the response
        }, status=status.HTTP_201_CREATED)

# UpdateView to handle updating an existing Book
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows for updating an existing book.
    Custom validation is added to ensure the 'publication_year' is not in the future.
    """
    queryset = Book.objects.all()  # Fetches all books
    serializer_class = BookSerializer  # Serializer for updating an existing book

    def perform_update(self, serializer):
        """
        Custom method to handle validation before updating a Book.
        Ensures the publication year is not in the future.
        """
        publication_year = serializer.validated_data.get('publication_year')  # Get the year from the request data
        current_year = datetime.now().year  # Get the current year
        if publication_year > current_year:
            raise ValidationError({'publication_year': 'The publication year cannot be in the future.'})  # Raise an error if year is in the future
        serializer.save()  # Save the changes if validation passes

    def update(self, request, *args, **kwargs):
        """
        Custom response on successful book update.
        """
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Book updated successfully!',
            'book': response.data  # Include the updated book data in the response
        }, status=status.HTTP_200_OK)

# DeleteView to handle removing a Book
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows for deleting an existing book.
    """
    queryset = Book.objects.all()  # Fetches all books
    serializer_class = BookSerializer  # Serializer to format the data when deleting (optional)
