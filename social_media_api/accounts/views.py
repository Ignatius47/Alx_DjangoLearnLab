from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, UserSerializer

# Ensure you're using the custom user model
CustomUser = get_user_model()

# Registration view
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({
                'user': UserSerializer(user, context={'request': request}).data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login view
class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user, context={'request': request}).data,
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# Follow and Unfollow viewset
class FollowViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    # Follow a user
    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user_to_follow = get_object_or_404(CustomUser, pk=pk)
        request.user.following.add(user_to_follow)  # Ensure `following` is a ManyToMany field
        return Response({'status': 'followed'}, status=status.HTTP_200_OK)

    # Unfollow a user
    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
        request.user.following.remove(user_to_unfollow)  # Ensure `following` is a ManyToMany field
        return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.IsAuthenticated
