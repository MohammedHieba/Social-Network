from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    # owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_image = models.ImageField(null=True, blank=True,
                                    upload_to='groups/images/', default='images/default_group.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through='Membership')


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
