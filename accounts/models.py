from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    pass
    # Male = "male"
    # Female = 'female'
    # GENDER = (
    #     (Male, "male"),
    #     (Female, "female"),
    # )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # gender = models.CharField(max_length=20, choices=GENDER, null=True)
    # birth_date = models.DateField(null=True, blank=True)
