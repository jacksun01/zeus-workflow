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
    if mod.owner:
        if mod.owner.find('#{}#'.format(instance.creator)) < 0:
            mod.owner = '{}{}#'.format(mod.owner, instance.creator)
    else:
        mod.owner = '#{}#'.format(instance.creator)
    mod.save()
    print('添加用户{}成功'.format(instance.creator))
    post_data = {'mod_id': mod.id, 'username': instance.creator}
    ret, err = request_post('http://www.zeus.com/api/v1/cicd/add_user/', post_data=post_data)
except Exception as e:
    print('脚本执行失败: {}'.format(e))
    print('task_mark_error=1')
