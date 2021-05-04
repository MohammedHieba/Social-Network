import django_filters
from django_filters import CharFilter
from .models import *


class UserFilter(django_filters.FilterSet):
    username = CharFilter(field_name="username", lookup_expr="icontains")

    class Meta:
        model: User
        exclude: '__all__'
