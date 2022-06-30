# -*- coding: utf-8 -*-
#author Jack qq:774428957
import json
import logging
from django.conf import settings
from utils.weixin_tool import Weixin
from utils.util import send_html_mail
from .models import *
from utils.dingding_tool import DingTalk

logger = logging.getLogger('views')
def workorder_notice(instance):
    '''工单通知'''
    STATUS = [
        (0,'已驳回'),
        (1,'新建中'),
        (2,'已提交,等待审批'),
        (3,'等待审批'),
        (4,'已处理,等待确认'),
        (5,'已结束'),
        (6,'未解决，等待确认并审批'),
    ]
    EXEC_STATUS = [
        (0, '待执行'),
        (1, '执行成功'),
        (2, '执行失败'),
        (3, '定时执行'),
    ]
    workorder_detail = get_workorder_detail(instance)
    ding_cli = DingTalk()
    data = json.loads(instance.data)
    if instance.cur_user:
        tos = instance.cur_user.email
        cc = ''
        if 'cc' in data: cc = data['cc']
        subject = '<{}>工单处理通知'.format(instance.cname)
        if instance.status == 2:
            ding_cli.send_workorder_approval_message(instance, workorder_detail, instance.cur_user.email, instance.cur_user.id)
            content = '<br>{}({})申请 {} 工单已发起，等待您处理，<a href="{}/#/workflow/workorderswaiting" target="_blank">点击处理工单</a>，谢谢！'.format(instance.creator.username, instance.creator.cname, instance.cname, settings.PROJECT_URL)
        elif instance.status == 3:
            ding_cli.send_workorder_approval_message(instance, workorder_detail, instance.cur_user.email, instance.cur_user.id)
            content = '<br>{}({})申请 {} 工单上级审批人已审批，等待您处理，<a href="{}/#/workflow/workorderswaiting" target="_blank">点击处理工单</a>，谢谢！'.format(instance.creator.username, instance.creator.cname, instance.cname, settings.PROJECT_URL)
        elif instance.status == 6:
            content = '<br>{}({})申请 {} 工单申请人反馈未解决，等待您确认并处理，<a href="{}/#/workflow/workorderswaiting" target="_blank">点击处理工单</a>，谢谢！'.format(instance.creator.username, instance.creator.cname, instance.cname, settings.PROJECT_URL)
        elif instance.status == 0:
            tos = instance.creator.email
            content = '<br>{} 工单已驳回，<a href="{}/#/workflow/workorders" target="_blank">点击查看</a>，谢谢！'.format(instance.cname, settings.PROJECT_URL)
        else:
            return ''
        #微信提醒
        im = instance.cur_user.im
        if im:
            weixin_config = {
                'WEIXIN_CORPID': settings.WORKFLOW_WEIXIN_CORPID,
                'WEIXIN_SECRET': settings.WORKFLOW_WEIXIN_SECRET,
                'WEIXIN_AGTID': settings.WORKFLOW_WEIXIN_AGTID,
            }
            weixin = Weixin(weixin_config)
            weixin.send_text(im, content.replace('<br>', ''))
        return send_html_mail(tos, subject, content, cc=cc)

def get_gitlab_groups(group_id=None):
    import gitlab
    gl = gitlab.Gitlab(settings.GITLAB_API, settings.GITLAB_ADMIN_TOTKEN)
    if group_id:
        ret = gl.groups.get(group_id)
    else:
        ret = gl.groups.list(per_page=100)
    return ret

def get_gitlab_projects(group_id):
    import gitlab
    gl = gitlab.Gitlab(settings.GITLAB_API, settings.GITLAB_ADMIN_TOTKEN)
    group = gl.groups.get(group_id)
    return group.projects.list(per_page=100)


def get_gitlab_group_auditors(group_id):
    import gitlab
    gl = gitlab.Gitlab(settings.GITLAB_API, settings.GITLAB_ADMIN_TOTKEN)
    group = gl.groups.get(group_id)
    return [row for row in group.members.list(all=True) if row.access_level == 40]

def get_strees(isone,deep,ishostpool,exclude2):
    from stree.util import get_strees
    return get_strees(isone=isone,deep=deep,ishostpool=ishostpool,exclude2=exclude2)

def get_stree_roles():
    from stree.models import StreeRole
    return StreeRole.objects.all()

def get_stree_auditors():
    from stree.models import StreeRole
    return StreeRole.objects.all()

def get_cicd_mods():
    from cicd.models import Mod
    return Mod.objects.filter(is_active=True)

def workorder_remind():
    data = {'code': 0, 'message': 'Success'}
    rets = WorkOrder.objects.filter(cur_step__role__name='dba')
    for ret in rets:
        subject = '【工单处理提醒】如已处理请忽略此邮件'
        content = '<br>{}({})申请 {} 工单已发起，工单ID{}, 申请时间{}, 等待您处理，<a href="{}/#/workflow/workorderswaiting" target="_blank">点击处理工单</a>，谢谢！'.format(
            ret.creator.username, ret.creator.cname, ret.cname, ret.id, ret.create_time.strftime('%Y-%m-%d %H:%M'), settings.PROJECT_URL)
        mail_list = [row.email for row in ret.cur_step.role.userprofile_set.all()]
        send_html_mail(','.join(mail_list), subject, content)
    return data


def get_workorder_detail(workorder_obj):
    workorder_detail = ""
    for item in json.loads(workorder_obj.data).keys():
        for workorder_formfield in json.loads(workorder_obj.formfields):
            if item == workorder_formfield["field"]:
                if workorder_formfield["options"]:
                    if isinstance(workorder_formfield["value"], list):
                        workorder_formfield_value = ''
                        for i in workorder_formfield["value"]:
                            for option in workorder_formfield["options"]:
                                if i == option["value"]:
                                    if workorder_formfield_value:
                                        workorder_formfield_value = str(workorder_formfield_value) + option["label"] + ","
                                    else:
                                        workorder_formfield_value = option["label"] + ","
                    else:
                        for option in workorder_formfield["options"]:
                            if workorder_formfield["value"] == option["value"]:
                                workorder_formfield_value = option["label"]
                else:
                    workorder_formfield_value = workorder_formfield["value"]
                workorder_detail = workorder_detail + workorder_formfield["title"] + ": " + str(workorder_formfield_value) + "\n\n"
                workorder_formfield_value = ""
    return workorder_detail
