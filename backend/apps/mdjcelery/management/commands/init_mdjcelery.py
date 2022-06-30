#coding:utf-8
#author Jack qq:774428957
from django.core.management.base import BaseCommand
from djcelery.models import TaskState, WorkerState, PeriodicTask, IntervalSchedule, CrontabSchedule
from users.models import Url, Role

init_data = [
    {
        'role':{'name':'mdjcelery_admin','cname':'任务调度管理员', 'description':'任务调度管理员'},
        'urls':[{'user_type': 'customuser', 'url':'^/api/v\d/mdjcelery/', 'method':'ALL'}]
    },
]
init_white_url_data = [
    #{'user_type': 'anonymous', 'url':'^/social/', 'method': 'ALL'},
    #{'user_type': 'authenticated', 'url':'^/api/v\d/users/user/', 'method': 'ALL'},
]
init_interval_data = [
    {'every': 5, 'period':'seconds'},
    {'every': 10, 'period':'seconds'},
    {'every': 30, 'period':'seconds'},
    {'every': 1, 'period':'minutes'},
    {'every': 2, 'period':'minutes'},
    {'every': 3, 'period':'minutes'},
    {'every': 5, 'period':'minutes'},
    {'every': 10, 'period':'minutes'},
    {'every': 20, 'period':'minutes'},
    {'every': 30, 'period':'minutes'},
    {'every': 1, 'period':'hours'},
    {'every': 2, 'period':'hours'},
    {'every': 6, 'period':'hours'},
    {'every': 12, 'period':'hours'},
    {'every': 1, 'period':'days'},
    {'every': 7, 'period':'days'},
]
init_crontab_data = [
    {'minute':'*','hour':'*','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'*/2','hour':'*','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'*/3','hour':'*','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'*/5','hour':'*','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'*/10','hour':'*','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'*/30','hour':'*','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'0','hour':'*','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'0','hour':'*/2','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'0','hour':'*/6','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'0','hour':'*/12','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'0','hour':'0','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'0','hour':'9','day_of_week':'*','day_of_month':'*','month_of_year':'*'},
    {'minute':'0','hour':'0','day_of_week':'0','day_of_month':'*','month_of_year':'*'},
]
init_task_data = [
    {
    'name': 'mdjcelery.tasks.test_task',
    'description':'测试定时任务',
    'task':'mdjcelery.tasks.test_task',
    'args':[],
    'kwargs':{},
    'crontab_id': 1
    #'crontab_id': CrontabSchedule.objects.get(minute='*',hour='*',day_of_week='*',day_of_month='*',month_of_year='*').id
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

        # IntervalSchedule
        for d in init_interval_data:
            IntervalSchedule.objects.get_or_create(**d)

        # CrontabSchedule
        for d in init_crontab_data:
            CrontabSchedule.objects.get_or_create(**d)

        # Task
        for d in init_task_data:
            PeriodicTask.objects.get_or_create(**d)

        print('init mdjcelery done')
