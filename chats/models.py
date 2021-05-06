from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class ChatQuerySet(models.query.QuerySet):
    def search_by_user(self, first_user: User, second_user: User):
        return self.filter(
            Q(first_user=first_user, second_user=second_user) |
            Q(first_user=second_user, second_user=first_user)
        )


class ChatManager(models.Manager):
    def get_queryset(self):
        return ChatQuerySet(self.model, using=self._db)

    def search_by_user(self, first_user, second_user):
        return self.get_queryset().search_by_user(first_user, second_user)


class Chat(models.Model):
    class Meta:
        unique_together = ['first_user', 'second_user']
        ordering = ['-last_updated_at']

    first_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='first_user')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='second_user')
    last_updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ChatManager()

    def __str__(self):
        return "ID:{chat} between {first_user} & {second_user}".format(
            chat=self.id,
            first_user=self.first_user.username,
            second_user=self.second_user.username,
        )

    @property
    def messages(self):
        return self.message_set.all()


class Message(models.Model):
    class Meta:
        db_table = 'messages'
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000, null=False)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
