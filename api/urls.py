from django.urls import path

from . import views

urlpatterns = [
    path('books/<int:pk>/', views.book_list, name='book_list'),
]