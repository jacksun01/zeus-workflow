#!/usr/bin/env python
#author Jack qq:774428957
#coding=utf-8
import os
import sys
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
from django.conf import settings
from workflow.models import WorkOrder
from utils.util import request_post
from cicd.util import create_gitlab_project

try:
    workorder_id = sys.argv[1]
    log_file = '{}/logs/workflow/{}.log'.format(settings.BASE_DIR, workorder_id)
    instance = WorkOrder.objects.get(pk=workorder_id)
    workflow = instance.workflow
    #Form表单数据
    data = json.loads(instance.data)
    print('python -u {} {} &>{}'.format(workflow.script.path, workorder_id, log_file))
    print('脚本开始执行')
    print('task_mark_percent=10')
    print('申请人是{}'.format(instance.creator))
    d = {}
    name = data['name']
    group_id = data['group_id']
    visibility = data['visibility']
    description = data['description']
    ret = create_gitlab_project(name,group_id,visibility,description)
    if ret.startswith('http'):
        print('新建项目地址是{}'.format(ret))
        url = 'http://apims.siku.cn/mock/51/project/open/create4Ops'
        post_data = {'code':workorder_id,'groupName':'mall','gitUrl':ret,'ownerName':instance.creator.username}
        r,err = request_post(url,post_data)
        if not err:
            data = r.json()
            code = data['code']
            if code == 0:
                print('自动创建代码骨架成功')
            else:
                print('自动创建代码骨架失败')
                print(data)
                print('task_mark_error=1')
        else:
            print('自动创建代码骨架失败')
            print(err)
            print('task_mark_error=1')
    else:
        print('脚本执行失败: {}'.format(ret))
        print('task_mark_error=1')
except Exception as e:
    print('脚本执行失败: {}'.format(e))
    print('task_mark_error=1')
# finally:
#     print('task_mark_percent=100')