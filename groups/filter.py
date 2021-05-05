import django_filters
from django_filters import CharFilter
from .models import *


class GroupsFilter(django_filters.FilterSet):
    search_name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model: User
        exclude: '__all__'
