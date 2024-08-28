from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view, signup, add_book, edit_book, delete_book

urlpatterns = [
    
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('signup/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin_view, name='admin'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
    path('book/add/', add_book, name='add-book'),
    path('book/<int:pk>/edit/', edit_book, name='edit-book'),
    path('book/<int:pk>/delete/', delete_book, name='delete-book'),
    path('books/', list_books, name='books'), 
    path('<int:id>/', LibraryDetailView.as_view(), name='library'),
    path('home/',index, name='index'),
    path('registration/',views.register,name='registration'),
    path('login/',login, name='login'),
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout' ),
    path('logout/',LoginView.as_view(template_name='relationship_app/login.html'), name='login' ),
    path('admin/', admin_view,name='adminview'),
    path('librarian/',librarian_view,name='librarianview'),
    path('member/',member_view,name='memberview'),
    path('add_book/',add_book, name='add_book'),
    path('edit_book/<int:id_book>/', edit_book, name='edit_book'),
    path('delete_book/<int:id_book>/', delete_book, name='delete_book'),
    

]
