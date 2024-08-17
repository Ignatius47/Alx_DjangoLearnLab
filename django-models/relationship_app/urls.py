from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('signup/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin_view, name='admin-view'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
    path('book/add/', add_book, name='add-book'),
    path('book/<int:pk>/edit/', edit_book, name='edit-book'),
    path('book/<int:pk>/delete/', delete_book, name='delete-book'),
    path('signup/', signup, name='register')
    path('login/', LoginView.as_view(template_name='yourapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='yourapp/logout.html'), name='logout'),
]
