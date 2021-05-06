from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from groups.models import Group


class NotificationQuerySet(models.query.QuerySet):
    def search_by_receiver_user(self, user, ordered=True):
        return self.filter(receiver=user).order_by(f"{'-' if ordered else ''}created_at")


class NotificationManager(models.Manager):
    def get_queryset(self):
        return NotificationQuerySet(self.model, using=self._db)

    def search_by_receiver_user(self, user):
        return self.get_queryset().search_by_receiver_user(user=user)


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
    notification_type = models.CharField(max_length=100, choices=NotificationTypes.choices,
                                         default=NotificationTypes.NOTIFY)
    is_seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = NotificationManager()

    @property
    def formatted_title(self):
        return self.title.format(sender=self.sender, title=self.title, redirect_to=self.redirect_to,
                                 receiver=self.receiver, group=self.group)

    @property
    def formatted_message(self):
        return self.message.format(sender=self.sender, title=self.formatted_title, redirect_to=self.redirect_to,
                                   receiver=self.receiver, group=self.group)

    @property
    def formatted_redirect_to(self):
        return f"{settings.SITE_URL}{self.redirect_to}"

    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.formatted_title} - {self.notification_type}"
