from django.shortcuts import render

# Create your views here.
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly

class BookListViewSet(viewsets.ModelViewset):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

