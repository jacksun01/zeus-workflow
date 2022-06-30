# -*- coding: utf-8 -*-
#author Jack qq:774428957
from django.db.models import Q
from django_filters import rest_framework as filters
from .models import *

class WorkOrderFilter(filters.FilterSet):
    action = filters.CharFilter(field_name='action', help_text='指令：sent(我的申请)、done(已审批)、waiting(待我审批)、supervise(督办)',method='filter_action')
    date_range = filters.DateRangeFilter(field_name='create_time', help_text='时间范围')

    def filter_action(self, queryset, name, value):
        if value == 'sent':
            return queryset.filter(creator=self.request.user)
        elif value == 'waiting':
            roles = self.request.user.roles.all()
            steps = AuditStep.objects.filter(role__in=roles)
            return queryset.filter((Q(status=2) | Q(status=3)),Q(exec_status=0)).filter(Q(cur_step__in=steps)|Q(cur_user=self.request.user))
        elif value == 'done':
            orders = [row.order.id for row in AuditRecord.objects.filter(user=self.request.user, opinion__lt=10)]
            return queryset.filter(id__in=orders)
        elif value == 'supervise':
            return queryset.filter((Q(status=2) | Q(status=3)),Q(exec_status=0))

    class Meta:
        model = WorkOrder
        fields = ('action', 'cur_user', 'status', 'date_range')