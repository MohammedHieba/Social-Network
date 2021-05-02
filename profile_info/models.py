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
