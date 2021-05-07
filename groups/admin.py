from django.contrib import admin

# Register your models here.
from groups.models import Group, Membership

admin.site.register(Group)
admin.site.register(Membership)