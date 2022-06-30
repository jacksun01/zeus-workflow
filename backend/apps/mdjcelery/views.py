# -*- coding: utf-8 -*-
#author Jack qq:774428957
import json
from rest_framework.decorators import action
from rest_framework import status
from djcelery.models import PeriodicTask, CrontabSchedule, IntervalSchedule
from utils.base_view import BaseModelViewSet, BaseGenericViewSet
from .filters import *
from .util import task_data_sync
from .serializers import *
from .models import *

class CrontabScheduleViewSet(BaseModelViewSet):
    """
    定时
    """
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabScheduleSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name','cname')

class IntervalScheduleViewSet(BaseModelViewSet):
    """
    间隔
    """
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name','cname')

class PeriodicTaskViewSet(BaseModelViewSet):
    """
    djcelery原生任务调度
    """
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name','cname')
    #filterset_class = IdcFilter

class TaskViewSet(BaseModelViewSet):
    """
    自定义封装任务调度
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name','cname')
    #filterset_class = IdcFilter

    @action(methods=['get'],detail=False)
    def get_table_info(self, request):
        '''
        获取表字段名和过滤选项
        '''
        data =  {}
        if hasattr(self.queryset.model(), 'get_fields'): data['fields'] = self.queryset.model().get_fields()
        return Response(data)

    def perform_create(self, serializer):
        instance = serializer.save()
        task_data_sync(instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        task_data_sync(instance)

    def perform_destroy(self, instance):
        PeriodicTask.objects.filter(name=instance.name).delete()
        instance.delete()

