from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowViewSet, RegisterAPIView, LoginAPIView

router = DefaultRouter()
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('', include(router.urls)),
    path('unfollow/<int:user_id>/', FollowViewSet.as_view({'post': 'unfollow'}), name='unfollow'),
    path('follow/<int:user_id>/', FollowViewSet.as_view({'post': 'follow'}), name='follow'),
]
