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
import gitlab
from django.conf import settings
from workflow.models import WorkOrder
from utils.util import request_post
from cicd.util import create_gitlab_project

try:
    gl = gitlab.Gitlab(settings.GITLAB_API, settings.GITLAB_ADMIN_TOTKEN)
    workorder_id = sys.argv[1]
    log_file = '{}/logs/workflow/{}.log'.format(settings.BASE_DIR, workorder_id)
    instance = WorkOrder.objects.get(pk=workorder_id)
    workflow = instance.workflow
    #Form表单数据
    data = json.loads(instance.data)
    gits = data['git']
    access_level = data['access_level']
    expires_at = data['expires_at']
    print('python -u {} {} &>{}'.format(workflow.script.path, workorder_id, log_file))
    print('脚本开始执行')
    print('申请人是{}'.format(instance.creator))
    print('申请Git项目是{}'.format(gits))
    users = gl.users.list(username=instance.creator)
    if users:
        user = users[0]
        git_list = [row.strip() for row in gits.split('\n')]
        for git in git_list:
            try:
                group_project = git.strip().replace('http://gitlab.zeus.com:8090/', '').replace('git@gitlab.zeus.com:', '')
                if group_project.endswith('.git'): group_project = group_project[:-4]
                project = gl.projects.get(group_project)
                if project:
                    members = project.members.list(query=instance.creator)
                    if instance.creator.username not in [row.username for row in members]:
                        project.members.create({'user_id': user.id, 'access_level': access_level, 'expires_at': expires_at})
                    else:
                        member = project.members.get(user.id)
                        member.access_level = access_level
                        member.expires_at = expires_at
                        member.save()
                    print('{}权限添加成功'.format(git))
            except Exception as e:
                print('脚本执行失败: {}'.format(e))
                print('task_mark_error=1')
    else:
        print('Gitlab系统中账户{}不存在，请先使用LDAP方式登录Gitlab完成账户自动注册'.format(instance.creator))
        print('task_mark_error=1')
except Exception as e:
    print('脚本执行失败: {}'.format(e))
    print('task_mark_error=1')
#finally:
    #print('task_mark_percent=100')