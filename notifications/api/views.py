from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from notifications.api.serializers import NotificationSerializer
from notifications.models import Notification


class ReadOnlyNotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.search_by_receiver_user(user=self.request.user)
