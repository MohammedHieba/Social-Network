from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Post(models.Model):
    class Meta:
        ordering = ('-created_at', )

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return f"{self.author} author | {self.created_at} created_on | body {self.body} "


class Comment(models.Model):
    class Meta:
        ordering = ('-created_at', )

    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')

    def __str__(self):
        return f"{self.author} author | {self.created_at} created_at | post {self.post} | comment {self.comment} "
