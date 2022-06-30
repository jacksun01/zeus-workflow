# -*- coding: utf-8 -*-
#author Jack qq:774428957
import re
import json
import datetime
import logging
from django.conf import settings
from djcelery.models import PeriodicTask, CrontabSchedule, IntervalSchedule

def task_data_sync(instance):
    d = {}
    d['name'] = instance.name
    d['description'] = instance.cname
    d['task'] = instance.task
    d['args'] = json.dumps(instance.args.split())
    d['expires'] = instance.expired_time
    d['enabled'] = instance.is_active
    if instance.crontab: d['crontab_id'] = instance.crontab.id
    if instance.interval: d['interval_id'] = instance.interval.id
    host = cmd = script_args = script_name = ''
    if instance.task == 'mdjcelery.tasks.local_script':
        script_name = instance.script.name
        script_args = instance.args
    elif instance.task == 'mdjcelery.tasks.remote_script':
        script_name = instance.script.name
        script_args = instance.args
        host = instance.host
    elif instance.task == 'mdjcelery.tasks.local_command':
        cmd = instance.cmd
    elif instance.task == 'mdjcelery.tasks.remote_command':
        cmd = instance.cmd
        host = instance.host
    d['kwargs'] = json.dumps({"script_args": script_args, "host": host, "cmd": cmd, "script_name": script_name})
    if PeriodicTask.objects.filter(name=instance.name):
        PeriodicTask.objects.filter(name=instance.name).update(**d)
    else:
        PeriodicTask.objects.create(**d)
    return d
