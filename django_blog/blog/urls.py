from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register,
    profile,
    post_detail, 
    edit_comment,
    delete_comment,
    search,
    posts_by_tag
)

urlpatterns = [

    # Auth views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # Post-related views
    path('posts/', PostListView.as_view(), name='post-list'),  # Changed this to 'posts/'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),

    # Comment-related views

    path('comments/<int:pk>/edit/', edit_comment, name='edit-comment'),
    path('comments/<int:pk>/delete/', delete_comment, name='delete-comment'),

    # Search and filter views
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('search/', search, name='search'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
]