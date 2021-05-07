from django.contrib import admin

from accounts.models import User
from profile_info.forms import SignUpForm


class DisplayUser(admin.ModelAdmin):
    form = SignUpForm

    class Meta:
        model = User


admin.site.register(User)
