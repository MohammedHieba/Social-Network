from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return f"{self.author} author | {self.created_on} created_on | body {self.body} "


# def validate_post(sender, instance, **kwargs):
#     num = Post.objects.filter(pk=instance.pk).count
#     if num == 0:
#         for word in instance.body:
#             words = ["bitch", "fuck"]
#             if word in words:
#                 raise Exception('NOt appropriate')
#
#     else:
#         print("update")
#
#
# pre_save.connect(validate_post, instance=Post)


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')

    def __str__(self):
        return f"{self.author} author | {self.created_on} created_on | post {self.post} | comment {self.comment} "
