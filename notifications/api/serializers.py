from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('formatted_title', 'formatted_message', 'formatted_redirect_to', 'created_at')
