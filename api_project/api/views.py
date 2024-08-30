from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from rest_framework import generics
>>>>>>> origin/main
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly

class BookViewSet():
    queryset = Book.objects.all(viewsets.ModelViewSet)
    serializer_class = BookSerializer
    permissions = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

<<<<<<< HEAD
=======
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
>>>>>>> origin/main
