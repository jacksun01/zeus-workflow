# -*- coding: utf-8 -*-
#author Jack qq:774428957
from django.db import models
from django.contrib.auth import get_user_model
from utils.base_model import BaseModel
from users.models import Role

User = get_user_model()

class WorkFlowGroup(BaseModel):
    order_num = models.IntegerField(verbose_name='排序', help_text='排序', blank=True, default=0)

    class Meta:
        unique_together = ('name',)
        verbose_name = "工作流分组"
        verbose_name_plural = verbose_name

class WorkFlow(BaseModel):
    def script_path(instance, filename):
        filename = '{}.py'.format(instance.name)
        return 'workflow/scripts/{}'.format(filename)

    description = models.TextField(verbose_name='描述', help_text='描述', blank=True, null=True)
    group = models.ForeignKey(WorkFlowGroup, verbose_name='工单组', help_text='工单组' ,blank=True, null=True, on_delete=models.SET_NULL)
    script = models.FileField(verbose_name='自动化脚本',help_text='自动化脚本', upload_to=script_path, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='是否启用',help_text='是否启用', default=True)
    num = models.IntegerField(verbose_name='工单数',help_text='工单数', blank=True, default=0)


    class Meta:
        unique_together = ('name',)
        verbose_name = "工作流配置"
        verbose_name_plural = verbose_name

class AuditStep(models.Model):
    ROLE_TYPE = (
        ('static', '静态角色'),
        ('dynamic', '动态角色'),
    )
    workflow = models.ForeignKey(WorkFlow, verbose_name='工作流', help_text='工作流', blank=True, null=True, on_delete=models.SET_NULL)
    role_type = models.CharField(verbose_name='角色类型', help_text='角色类型', choices=ROLE_TYPE, default='static', max_length=16)
    role = models.ForeignKey(Role, verbose_name='角色', help_text='角色', blank=True, null=True, on_delete=models.SET_NULL)
    url = models.CharField(verbose_name='动态审批人API', help_text='动态审批人API', max_length=1024, blank=True, null=True)
    order_num = models.IntegerField(verbose_name='排序',help_text='排序', blank=True, default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', auto_now_add=True)

    class Meta:
        #unique_together = ('workflow', 'order_num')
        verbose_name = '工作流审批流程'
        verbose_name_plural = verbose_name

class FormField(models.Model):
    """自定义表单字段"""
    FIELD_TYPE = (
        ('input', '输入框'),
        ('InputNumber', '数字输入框'),
        ('DatePicker', '日期'),
        ('TimePicker', '日期时间'),
        ('switch', '开关'),
        ('radio', '单选框'),
        ('checkbox', '多选框'),
        ('select', '下拉框'),
        ('textarea', '文本域'),
        ('cascader', '级联选择器'),
        ('upload', '上传'),
        ('hidden', '隐藏域'),
    )
    workflow = models.ForeignKey(WorkFlow, verbose_name='工作流', help_text='工作流', blank=True, null=True, on_delete=models.SET_NULL)
    type = models.CharField(verbose_name='组件类型', help_text='组件类型', choices=FIELD_TYPE, max_length=32)
    field = models.CharField(verbose_name='字段名', help_text='字段名', max_length=32)
    title = models.CharField(verbose_name='标题', help_text='标题', max_length=32)
    value = models.TextField(verbose_name='字段值', help_text='字段值', default='', blank=True, null=True)
    props = models.TextField(verbose_name='属性', help_text='属性', blank=True, null=True)
    validate = models.TextField(verbose_name='数据校验', help_text='数据校验', blank=True,null=True)
    options = models.TextField(verbose_name='选项数据', help_text='选项数据', blank=True,null=True)
    dicurl = models.CharField(verbose_name='选项数据接口', help_text='选项数据接口', max_length=1024, blank=True,null=True)
    order_num = models.IntegerField(verbose_name='排序', help_text='排序',default=0, blank=True)
    is_active = models.BooleanField(verbose_name='是否启用',help_text='是否启用', default=True)

    class Meta:
        unique_together = ('workflow', 'field')
        verbose_name = '工作流自定义字段'
        verbose_name_plural = verbose_name

class WorkOrder(BaseModel):
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

    workflow = models.ForeignKey(WorkFlow, verbose_name='工作流', help_text='工作流', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(verbose_name='描述', help_text='描述', blank=True, null=True)
    creator = models.ForeignKey(User, verbose_name='申请人', help_text='申请人', related_name='creator', blank=True, null=True,on_delete=models.SET_NULL)
    steps = models.TextField(verbose_name='审批流',help_text='审批流', blank=True, null=True)
    formfields = models.TextField(verbose_name='表单字段',help_text='表单字段', blank=True, null=True)
    data = models.TextField(verbose_name='表单数据',help_text='表单数据', blank=True, null=True)
    file_info = models.TextField(verbose_name="附件信息",help_text="附件信息",blank=True, null=True)
    status = models.IntegerField(verbose_name='状态', help_text='状态',choices=STATUS, default=STATUS[1][0])
    exec_status = models.IntegerField(verbose_name='执行状态', help_text='执行状态',choices=EXEC_STATUS, default=EXEC_STATUS[0][0])
    exec_log = models.TextField(verbose_name='执行日志', help_text='执行日志',blank=True, null=True)
    cur_step = models.ForeignKey(AuditStep, verbose_name='当前审批流',help_text='当前审批流',blank=True, null=True, on_delete=models.SET_NULL)
    cur_user = models.ForeignKey(User, verbose_name='当前处理人',help_text='当前处理人', related_name='cur_user', blank=True, null=True,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "工单"
        verbose_name_plural = verbose_name

class AuditRecord(models.Model):
    OPINION = [
        #审批人意见
        (1, '同意'),
        (0, '驳回'),
        (2, '同意，已手动执行完成'),
        (3, '移交工单'),
        # (3, '回退修改'),
        #申请人反馈
        (10, '已解决'),
        (11, '未解决'),
    ]
    order = models.ForeignKey(WorkOrder, verbose_name='工单', help_text='工单', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='审批人', help_text='审批人', blank=True, null=True, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name='角色',help_text='角色',blank=True, null=True,on_delete=models.CASCADE)
    opinion = models.IntegerField(verbose_name='处理意见', help_text='处理意见',choices=OPINION)
    remark = models.TextField(verbose_name='说明', help_text='说明',blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='审批时间',help_text='审批时间',auto_now_add=True)

    class Meta:
        verbose_name = "工单审批记录"
        verbose_name_plural = verbose_name

class Guestbook(models.Model):
    order = models.ForeignKey(WorkOrder, verbose_name='工单', help_text='工单', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='用户', help_text='用户', blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='留言内容', help_text='留言内容',blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='留言时间', help_text='留言时间', auto_now_add=True)

    class Meta:
        verbose_name = "工单留言板"
        verbose_name_plural = verbose_name