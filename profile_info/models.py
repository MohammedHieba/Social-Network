from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER = (
        ("male", "male"),
        ("female", "female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(null=False, blank=False,
                                      upload_to='users/images/', default='images/default.jpg')


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


# class Friends(models.Model):
#     pass
