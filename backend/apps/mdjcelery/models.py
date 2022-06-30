# -*- coding: utf-8 -*-
from django.db import models
from djcelery.models import PeriodicTask, CrontabSchedule, IntervalSchedule
from utils.base_model import BaseModel

class Task(BaseModel):
    TASK = (
        ('mdjcelery.tasks.local_command', '执行本地Shell命令'),
        ('mdjcelery.tasks.local_script', '执行本地脚本'),
        ('mdjcelery.tasks.remote_command', '执行远程Shell命令'),
        ('mdjcelery.tasks.remote_script', '执行远程脚本'),
    )
    def script_path(instance, filename):
        filename = '{}.py'.format(instance.name)
        return 'mdjcelery/scripts/{}'.format(filename)

    task = models.CharField(verbose_name='任务类型', help_text='任务类型', max_length=32, blank=True, null=True)
    script = models.FileField(verbose_name='脚本', help_text='脚本', upload_to=script_path, blank=True, null=True)
    args = models.CharField(verbose_name='脚本参数', help_text='脚本参数', max_length=256, blank=True, null=True)
    host = models.CharField(verbose_name='远程主机', help_text='远程主机', max_length=256, blank=True, null=True)
    cmd = models.TextField(verbose_name='shell命令', help_text='shell命令', blank=True, null=True)
    crontab = models.ForeignKey(CrontabSchedule, verbose_name='定时', help_text='定时', blank=True, null=True, on_delete=models.SET_NULL)
    interval = models.ForeignKey(IntervalSchedule, verbose_name='间隔', help_text='间隔', blank=True, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(verbose_name='是否启用', help_text='是否启用', default=True)
    expired_time = models.DateField(verbose_name='过期时间', help_text='过期时间', blank=True, null=True)

    class Meta:
        unique_together = ('name',)
        verbose_name = "任务调度"
        verbose_name_plural = verbose_name
