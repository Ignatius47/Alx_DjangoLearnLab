from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    list_books, LibraryDetailView, librarian_view, member_view,
    add_book, edit_book, delete_book, index, register, admin_view
)



urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
    path('book/add/', add_book, name='add-book'),
    path('book/<int:pk>/edit/', edit_book, name='edit-book'),
    path('book/<int:pk>/delete/', delete_book, name='delete-book'),
    path('home/', index, name='index'),
    path('registration/', register, name='registration'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', admin_view, name='adminview'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)