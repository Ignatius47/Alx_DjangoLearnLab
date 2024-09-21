from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Notification
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        notifications = request.user.notifications.filter(read=False).order_by('-timestamp')
        data = [{
            'actor': n.actor.username,
            'verb': n.verb,
            'target': str(n.target),
            'timestamp': n.timestamp,
        } for n in notifications
        ]
        return Response(data)
    
    @action(detail=True, methods=['post'], permission_classes=IsAuthenticated)
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.read = True
        notification.save()
        return Response({'message': 'read'})