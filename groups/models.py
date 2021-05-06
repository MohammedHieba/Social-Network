from accounts.models import User
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    group_image = models.ImageField(null=True, blank=True,
                                    upload_to='groups/images/', default='images/default_group.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
