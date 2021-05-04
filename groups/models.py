from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    group_image = models.ImageField(null=True, blank=True,
                                    upload_to='groups/images/',
                                    default='images/default_group.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
