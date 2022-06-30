# -*- coding: utf-8 -*-
#author Jack qq:774428957
from djcelery.models import TaskState, WorkerState, PeriodicTask, IntervalSchedule, CrontabSchedule
from xadmin.sites import site
from .models import *

class TaskAdmin(object):
    list_display = ['name', 'cname','create_time']

site.register(Task, TaskAdmin)
site.register(IntervalSchedule) # 存储循环任务设置的时间
site.register(CrontabSchedule) # 存储定时任务设置的时间
site.register(PeriodicTask) # 存储任务
site.register(TaskState) # 存储任务执行状态
site.register(WorkerState) # 存储执行任务的worker