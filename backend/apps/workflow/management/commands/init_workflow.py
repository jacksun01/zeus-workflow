#coding:utf-8
#author Jack qq:774428957
from django.core.management.base import BaseCommand
from djcelery.models import PeriodicTask, CrontabSchedule, IntervalSchedule
from users.models import Url, Role
from workflow.models import *

init_data = [
    {
        'role':{'name':'workflow_admin','cname':'工作流管理员', 'description':'工作流管理员'},
        'urls':[{'user_type': 'customuser', 'url':'^/api/v\d/workflow/', 'method':'ALL'}]
    },
    {
        'role': {'name': 'workflow_supervisor', 'cname': '工作流督办人', 'description': '工作流督办人'},
        'urls': [{'user_type': 'customuser', 'url': '^/api/v\d/workflow/workorderssupervise/', 'method': 'GET'},]
    },
]

init_white_url_data = [
    {'user_type': 'authenticated', 'url':'^/api/v\d/workflow/workorders/', 'method': 'ALL'},
    {'user_type': 'authenticated', 'url':'^/api/v\d/workflow/workflows/\d+/', 'method': 'GET'},
    {'user_type': 'authenticated', 'url':'^/api/v\d/workflow/auditsteps/', 'method': 'GET'},
    {'user_type': 'authenticated', 'url':'^/api/v\d/workflow/records/', 'method': 'GET'},
    {'user_type': 'authenticated', 'url':'^/api/v\d/workflow/openapis/', 'method': 'ALL'},
    # 控制前端导航显示
    {'user_type': 'authenticated', 'url':'^/api/v\d/workflow/workorderswaiting/', 'method': 'GET'},
]

init_demo_workorder_field_data = [
    { "type":"input", "field":"name_a", "title":"输入框", "validate":"", "order_num":2},
    { "type":"switch", "field":"test", "title":"开关", "value":"", "order_num":3},
    { "type":"DatePicker", "field":"date", "title":"日期y-m-d", "value":"", "order_num":6},
    { "type":"TimePicker", "field":"time", "title":"时间H:M:S", "value":"", "props":"", "order_num":7},
    { "type":"DatePicker", "field":"datetime", "title":"日期时间", "value":"", "props":"{\"type\":\"datetime\",\"format\":\"yyyy-MM-dd HH:mm:ss\",\"placeholder\":\"请选择日期\"}", "order_num":8},
    { "type":"DatePicker", "field":"date_range", "title":"时间段", "value":"", "props":"{\"type\":\"datetimerange\",\"format\":\"yyyy-MM-dd HH:mm:ss\",\"placeholder\":\"请选择日期\"}", "order_num":9},
    { "type":"radio", "field":"radio", "title":"单选", "value":"", "options":"[{\"value\":\"0\",\"label\":\"包邮\",\"disabled\":false},{\"value\":\"1\",\"label\":\"不包邮\",\"disabled\":false}]", "order_num":11},
    { "type":"checkbox", "field":"checkbox", "title":"多选", "value":"", "options":"[{\"value\":\"0\",\"label\":\"大象\",\"disabled\":false},{\"value\":\"1\",\"label\":\"青蛙\",\"disabled\":false},{\"value\":\"2\",\"label\":\"狐狸\",\"disabled\":false}]", "order_num":13},
    { "type":"select", "field":"select", "title":"下拉框", "value":"", "options":"[{\"value\":\"0\",\"label\":\"大象\",\"disabled\":false},{\"value\":\"1\",\"label\":\"青蛙\",\"disabled\":false},{\"value\":\"2\",\"label\":\"狐狸\",\"disabled\":false}]", "order_num":15},
    { "type":"select", "field":"select_mul", "title":"下拉-多选", "value":"0", "props":"{\"multiple\":true,\"filterable\":true}", "options":"[{\"value\":\"0\",\"label\":\"大象\",\"disabled\":false},{\"value\":\"1\",\"label\":\"青蛙\",\"disabled\":false},{\"value\":\"2\",\"label\":\"狐狸\",\"disabled\":false}]", "order_num":17},
    { "type":"hidden", "field":"hidden", "title":"隐藏域", "value":"", "order_num":18},
]

init_crontab_data = [
    {
        'name': 'workflow.tasks.workorder_remind_task',
        'description': '工单审批提醒',
        'task': 'workflow.tasks.workorder_remind_task',
        'args': [],
        'kwargs': {},
        'crontab_id': CrontabSchedule.objects.get_or_create(minute='0', hour='*/2', day_of_week='*', day_of_month='*',
                                                  month_of_year='*')[0].id
    },
]

class Command(BaseCommand):

    def handle(self, *args, **options):

        #角色权限
        for d in init_data:
            role,created = Role.objects.get_or_create(**d['role'])
            for row in d['urls']:
                url,created  = Url.objects.get_or_create(**row)
                role.urls.add(url)
            role.save()

        #URL权限白名单
        for d in init_white_url_data:
            Url.objects.get_or_create(**d)

        # 定时任务
        for d in init_crontab_data:
            PeriodicTask.objects.get_or_create(**d)

        # demo
        workflow_group,created = WorkFlowGroup.objects.get_or_create(name='other',cname='其他问题')
        workflow,created = WorkFlow.objects.get_or_create(name='demo',cname='DEMO',group=workflow_group, is_active=False)
        for row in init_demo_workorder_field_data:
            row['workflow'] = workflow
            FormField.objects.get_or_create(**row)

        print('init workflow done')
