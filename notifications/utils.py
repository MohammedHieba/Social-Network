from django.conf import settings
from accounts.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from notifications.api.serializers import NotificationSerializer
from notifications.models import Notification
from asgiref.sync import async_to_sync
import channels.layers


def notify(sender: User, receiver: User, title: str, message: str, redirect_to: str, group=None,
           notify_type=Notification.NotificationTypes.NOTIFY) -> Notification:
    notification =  Notification.objects.create(sender=sender, receiver=receiver, title=title, message=message, group=group,
                                       redirect_to=redirect_to, notification_type=notify_type)
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_1", {"type": "notification_message", 'message': NotificationSerializer(notification).data})
    return notification


def notify_and_email(sender: User, receiver: User, title: str, message: str, redirect_to: str,
                     group=None) -> Notification:
    notification = notify(sender=sender, receiver=receiver, title=title, message=message, redirect_to=redirect_to,
                          group=group, notify_type=Notification.NotificationTypes.NOTIFY_WITH_EMAIL)
    if notification:
        html_message = render_to_string('notifications/email.html', {'notification': notification})
        send_mail(subject=notification.formatted_title,
                  message=strip_tags(html_message),
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[notification.receiver.email],
                  fail_silently=True,
                  html_message=html_message)
    return notification
