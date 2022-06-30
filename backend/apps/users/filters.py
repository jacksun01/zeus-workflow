# -*- coding: utf-8 -*-
#author Jack qq:774428957
from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()


class UrlFilter(filters.FilterSet):
    class Meta:
        model = Url
        fields = ('user_type', 'method', )


class UsersFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ('is_active', 'is_superuser', 'is_staff',)

class RoleFilter(filters.FilterSet):
    class Meta:
        model = Role
        fields = ('urls', )

