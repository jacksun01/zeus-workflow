#coding=utf-8
#author Jack qq:774428957
import os
import sys
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.core.management import execute_from_command_line
from django.conf import settings
from workflow.models import WorkOrder
from cicd.util import add_job_rule_white
from cicd.models import Mod
from utils.util import request_post

try:
    workorder_id = sys.argv[1]
    log_file = '{}/logs/workflow/{}.log'.format(settings.BASE_DIR, workorder_id)
    instance = WorkOrder.objects.get(pk=workorder_id)
    data = json.loads(instance.data)
    print('python -u {} {} &>{}'.format(os.path.abspath(__file__), workorder_id, log_file))
    print('脚本开始执行')
    print('申请人是{}'.format(instance.creator))
    mod = Mod.objects.get(pk=data['mod_id'])
    if add_job_rule_white(mod.name,instance.creator,data['expires_at']):
        print('授权成功，{}小时后权限将自动过期！'.format(data['expires_at']))
    else:
        print('授权失败，请联系运维同学！')
        print('task_mark_error=1')
except Exception as e:
    print('脚本执行失败: {}'.format(e))
    print('task_mark_error=1')