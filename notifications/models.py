from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from groups.models import Group


class Notification(models.Model):
    class NotificationTypes(models.TextChoices):
        NOTIFY = 'N', _('Notify')
        NOTIFY_WITH_EMAIL = 'NE', _('Notify With Email')

    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='notification_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='notification_receiver')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=255)
    redirect_to = models.CharField(max_length=255, null=True)
    notification_type = models.CharField(max_length=100, choices=NotificationTypes.choices, default=NotificationTypes.NOTIFY)
    created_at = models.DateTimeField(auto_now_add=True)
