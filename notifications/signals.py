from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from chats.models import Message
from notifications.utils import notify_and_email


@receiver(post_save, sender=Message)
def send_message(sender, instance: Message, created: bool, *args, **kwargs):
    if created:
        to = instance.chat.second_user if instance.chat.first_user == instance.by else instance.chat.first_user
        title = "{sender} has sent you message"
        message = "{title}: " + instance.message + ". tap on the following button to reply."
        redirect_to = reverse('Chats:show', kwargs={'id': instance.chat_id})
        notify_and_email(instance.by, to, title, message, redirect_to)

