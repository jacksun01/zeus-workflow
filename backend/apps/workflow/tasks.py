#coding:utf-8
#author Jack qq:774428957
import os
import re
from django.conf import settings
from celery import task
from utils.util import local_cmd,send_html_mail
from .models import WorkOrder
from .util import workorder_remind

@task()
def workorder_task(workorder_id):
    instance = WorkOrder.objects.get(pk=workorder_id)
    cname = instance.cname
    creator = instance.creator
    exec_status = 1
    script_path = instance.workflow.script.path
    if os.path.exists(script_path):
        log_file = '{}/logs/workflow/{}.log'.format(settings.BASE_DIR, workorder_id)
        cmd = 'python -u {} {} &>>{}'.format(script_path, workorder_id, log_file)
        local_cmd(cmd)
        with open(log_file) as file:
            log_content = file.read()
        m = re.search('task_mark_error', log_content, re.M)
        if m: exec_status = 2
        m = re.search('task_mark_crontab', log_content, re.M)
        if m: exec_status = 3
        instance.exec_log = log_content
    instance.exec_status = exec_status
    instance.save()
    tos = creator.email
    subject = '<{}>工单进度通知'.format(cname)
    content = '<br>您好！<br>{} 工单已处理，等待您确认，<a href="{}/#/workflow/workorderswaiting" ' \
              'target="_blank">点击此处处理工单</a>，<a href="{}/#/workflow/workorderswaiting" target="_blank">点击此处查看工单详情</a>，' \
              '谢谢！'.format(
        instance.cname, settings.PROJECT_URL, instance.id, settings.PROJECT_URL, instance.id)
    send_html_mail(tos, subject, content)
    return 'workorder task done'

@task()
def workorder_remind_task():
    workorder_remind()
    return 'workorder notice task done'