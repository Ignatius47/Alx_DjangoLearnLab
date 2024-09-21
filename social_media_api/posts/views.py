from django.shortcuts import render
from .serializers import CommentSerializer, PostSerializer
from rest_framework import viewsets, permissions, filters, generics
from .models import Post, Comment, Like
from .permissions import IsAuthorOrReadOnly
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from django.contrib.auth import get_user_model
from rest_framework.decorators import action

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')  # Latest posts first
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)  # Fetch the post using generics.get_object_or_404
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # Create a notification for the post's author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                action_object=post
            )
        return Response({'detail': 'Liked'}, status=201)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)  # Fetch the post using generics.get_object_or_404
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
        return Response({'detail': 'Unliked'}, status=204)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        post = generics.get_object_or_404(Post, pk=self.request.data.get('post_id'))  # Ensure post is fetched
        serializer.save(author=self.request.user, post=post)
        
        # Create a notification for the post's author when a comment is made
        Notification.objects.create(
            recipient=post.author,
            actor=self.request.user,
            verb='commented on your post',
            action_object=post
        )


class FeedView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get the current user's following list
        following_users = request.user.following.all()  # Assuming `following` is a ManyToManyField to User

        # Fetch posts from the users they are following, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)

    def list(self, request):
        posts = Post.objects.filter(author__in=request.user.following.all()).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
