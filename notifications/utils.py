from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from notifications.models import Notification


def formatted_notification(notification: Notification) -> str:
    formatted_message = notification.message.format(
        sender=notification.sender,
        title=notification.title,
        redirect_to=notification.redirect_to,
        receiver=notification.receiver,
        group=notification.group
    )
    return formatted_message


def notify(sender: User, receiver: User, title: str, message: str, redirect_to: str, group=None,
           notify_type=Notification.NotificationTypes.NOTIFY) -> Notification:
    return Notification.objects.create(sender=sender, receiver=receiver, title=title, message=message, group=group,
                                       redirect_to=redirect_to, notification_type=notify_type)


def notify_and_email(sender: User, receiver: User, title: str, message: str, redirect_to: str,
                     group=None) -> Notification:
    notification = notify(sender=sender, receiver=receiver, title=title, message=message, redirect_to=redirect_to,
                          group=group, notify_type=Notification.NotificationTypes.NOTIFY_WITH_EMAIL)
    if notification:
        message = formatted_notification(notification)
        html_message = render_to_string('notifications/email.html', {'notification': notification, 'message': message})
        send_mail(subject=notification.title,
                  message=strip_tags(html_message),
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=[notification.receiver.email],
                  fail_silently=True,
                  html_message=html_message)
    return notification
