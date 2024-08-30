from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . views import BookListViewSet
from rest_framework.authtoken import views as drf_views

router = DefaultRouter()
router.register(r'books', BookListViewSet)

urlpatterns = [
    path('books/<int:pk>/', views.book_list, name='book_list'),
    path('', include(router.urls)),
    path('api-token-auth/', drf_views.obtain_auth_token, name='api_token_auth'),
]