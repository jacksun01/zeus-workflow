# -*- coding: utf-8 -*-
#author Jack qq:774428957
from django_filters import rest_framework as filters
from .models import LogsEntry


class LogsEntryFilter(filters.FilterSet):
    date_range = filters.DateRangeFilter(field_name='time_added', help_text='时间范围')

    class Meta:
        model = LogsEntry
        fields = ('user', 'content_type','action_flag', 'date_range')