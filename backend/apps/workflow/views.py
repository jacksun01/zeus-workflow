# -*- coding: utf-8 -*-
#author Jack qq:774428957
import json
import logging
from django.conf import settings
from django.db.models import Q, Count
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from utils.base_view import BaseModelViewSet, BaseGenericViewSet
from users.models import Role
from .util import *
from .tasks import workorder_task
from .serializers import *
from .models import *
from .filters import *
from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse

User = get_user_model()

logger = logging.getLogger('views')


class WorkFlowGroupViewSet(BaseModelViewSet):
    queryset = WorkFlowGroup.objects.order_by('order_num')
    serializer_class = WorkFlowGroupSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name', 'cname')
    # filterset_class = IdcFilter


class FormFieldViewSet(BaseModelViewSet):
    queryset = FormField.objects.order_by('order_num')
    serializer_class = FormFieldSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name', 'cname')

    # filterset_class = IdcFilter

    @action(methods=['get'], detail=True)
    def up(self, request, pk):
        '''
        向上移动
        '''
        instance = self.get_object()
        last_instance = self.queryset.filter(workflow=instance.workflow, order_num__lt=instance.order_num).last()
        if last_instance:
            last_instance.order_num, instance.order_num = instance.order_num, last_instance.order_num
            last_instance.save()
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def down(self, request, pk):
        '''
        向下移动
        '''
        instance = self.get_object()
        next_instance = self.queryset.filter(workflow=instance.workflow, order_num__gt=instance.order_num).first()
        if next_instance:
            next_instance.order_num, instance.order_num = instance.order_num, next_instance.order_num
            next_instance.save()
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AuditStepViewSet(BaseModelViewSet):
    queryset = AuditStep.objects.order_by('order_num')
    serializer_class = AuditStepSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name', 'cname')

    @action(methods=['get'], detail=True)
    def up(self, request, pk):
        '''
        向上移动
        '''
        instance = self.get_object()
        last_instance = self.queryset.filter(workflow=instance.workflow, order_num__lt=instance.order_num).last()
        if last_instance:
            last_instance.order_num, instance.order_num = instance.order_num, last_instance.order_num
            last_instance.save()
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def down(self, request, pk):
        '''
        向下移动
        '''
        instance = self.get_object()
        next_instance = self.queryset.filter(workflow=instance.workflow, order_num__gt=instance.order_num).first()
        if next_instance:
            next_instance.order_num, instance.order_num = instance.order_num, next_instance.order_num
            next_instance.save()
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def get_table_info(self, request):
        '''
        获取表字段名和过滤选项
        '''
        # option = request.query_params.get('option', '')
        data = {}
        if hasattr(self.queryset.model(), 'get_fields'): data['fields'] = self.queryset.model().get_fields()
        data['role_types'] = AuditStep.ROLE_TYPE
        data['roles'] = [{'id': row.id, 'cname': row.cname} for row in Role.objects.all()]
        return Response(data)


class WorkFlowViewSet(BaseModelViewSet):
    queryset = WorkFlow.objects.order_by('-id')
    serializer_class = WorkFlowSerializer
    ordering_fields = ('id', 'name', 'num')
    search_fields = ('name', 'cname')

    # filterset_class = WorkFlowFilter

    @action(methods=['get'], detail=True)
    def steps(self, request, pk):
        '''
        审批流
        '''
        instance = self.get_object()
        step_instances = AuditStep.objects.filter(workflow=instance).order_by('order_num')
        serializer = AuditStepSerializer(step_instances, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def formfields(self, request, pk):
        '''
        表单字段
        '''
        instance = self.get_object()
        formfield_instances = FormField.objects.filter(workflow=instance).order_by('order_num')
        serializer = FormFieldSerializer(formfield_instances, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def demoformfields(self, request):
        '''
        demo表单字段
        '''
        instance = WorkFlow.objects.get(name='demo')
        formfield_instances = FormField.objects.filter(workflow=instance).order_by('order_num')
        serializer = FormFieldSerializer(formfield_instances, many=True)
        return Response(serializer.data)


class WorkOrderViewSet(BaseModelViewSet):
    queryset = WorkOrder.objects.order_by('-id')
    serializer_class = WorkOrderSerializer
    ordering_fields = ('id', 'name')
    search_fields = ('id', 'name', 'cname', 'creator__username', 'cur_user__username')
    filterset_class = WorkOrderFilter

    def get_serializer_class(self):
        if self.action == 'audit':
            return AuditSerializer
        elif self.action == 'list':
            return WorkOrderListSerializer
        elif self.action == 'auditrecord':
            return AuditRecordSerializer
        elif self.action == 'feedback':
            return FeedbackSerializer
        elif self.action == 'guestbook':
            return GuestbookSerializer
        elif self.action == 'create':
            return CreateWorkOrderSerializer
        elif self.action == 'revoke':
            return RevokeSerializer
        else:
            return self.serializer_class

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.creator = self.request.user
        instance.name = instance.workflow.name
        instance.cname = instance.workflow.cname
        steps = instance.workflow.auditstep_set.order_by('order_num')
        instance.steps = json.dumps(AuditStepSerializer(steps, many=True).data)
        instance.status = 2
        instance.workflow.num += 1
        instance.workflow.save()
        #先保存，如果免审核工单需要用到用户信息
        instance.save()
        # 免审批
        if not steps:
            instance.cur_step = None
            instance.cur_user = self.request.user
            if hasattr(instance.workflow, 'script'):
                workorder_task.apply_async((instance.id,), queue=settings.HIGH_PRIORITY_QUEUE)
                instance.status = 4
        else:
            instance.cur_step = steps[0]
        instance.save()
        # 邮件通知
        workorder_notice(instance)
        # return Response({'code': 0, 'msg': 'success'},)

    @action(methods=['get'], detail=False)
    def get_table_info(self, request):
        '''
        获取表字段名和过滤选项
        '''
        # option = request.query_params.get('option', '')
        data = {}
        if hasattr(self.queryset.model(), 'get_fields'): data['fields'] = self.queryset.model().get_fields()
        group_data = []
        workflow_data = []
        for row in WorkFlowGroup.objects.order_by('order_num'):
            d = {}
            d['id'] = row.id
            d['name'] = row.name
            d['cname'] = row.cname
            workflows = WorkFlow.objects.filter(is_active=True, group=row).order_by('-num')
            d['workflow'] = [{'id': i.id, 'name': i.name, 'cname': i.cname} for i in workflows]
            group_data.append(d)
        for row in WorkFlow.objects.filter(is_active=True, num__gt=0).order_by('-num')[:15]:
            d = {}
            d['id'] = row.id
            d['name'] = row.name
            d['cname'] = row.cname
            d['num'] = row.num
            d['group_cname'] = row.group.cname
            workflow_data.append(d)
        data['workflowgroups'] = group_data
        data['workflows'] = workflow_data
        data['exec_statuss'] = WorkOrder.EXEC_STATUS
        data['statuss'] = WorkOrder.STATUS
        return Response(data)


    @action(methods=['post'], detail=True)
    def audit(self, request, pk):
        '''
        审批工单
        '''
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        next_user = instance.creator
        if 'next_user' in serializer.data:
            next_user = serializer.validated_data['next_user']
        opinion = serializer.validated_data["opinion"]
        remark = serializer.validated_data["remark"]
        cur_step = instance.cur_step
        if not cur_step: return Response({'detail': ['流程已更新，您不是当前审批人']}, status=status.HTTP_400_BAD_REQUEST)
        cur_role = cur_step.role
        cur_users = cur_role.userprofile_set.all()
        roles = ['super_admin', 'workflow_supervisor', 'workflow_admin']
        is_supervisor = True if request.user.roles.filter(name__in=roles) else False
        if request.user != instance.cur_user and request.user not in cur_users and not is_supervisor:
            return Response({'detail': ['流程已更新，您不是当前审批人']}, status=status.HTTP_400_BAD_REQUEST)
        steps = AuditStep.objects.filter(workflow=instance.workflow).order_by('order_num')
        next_step = steps.filter(order_num__gt=cur_step.order_num).first()
        data = {}
        data['order'] = instance
        data['user'] = request.user
        data['role'] = cur_role
        if request.user not in cur_users and is_supervisor: data['role'] = Role.objects.get(name='workflow_supervisor')
        data['opinion'] = opinion
        data['remark'] = remark
        AuditRecord.objects.create(**data)

        # 1. 审批人不是工单流程最后审批人
        if cur_step != steps.last():
            # 驳回
            if opinion == 0:
                next_step = None
                next_status = 0
                next_user = None
            # 同意
            elif opinion == 1 or opinion == 2:
                next_step = next_step
                next_status = 3
            # 移交
            elif opinion == 3:
                next_step = cur_step
                next_status = instance.status
        # 2. 审批人是工单流程最后审批人
        elif cur_step == steps.last():
            # 驳回
            if opinion == 0:
                next_step = None
                next_status = 0
                next_user = None
                instance.exec_status = 1
            # 同意
            elif opinion == 1:
                next_step = None
                next_status = 4
                next_user = None
                instance.status = next_status
                instance.save()
                workorder_task.apply_async((instance.id,), queue=settings.HIGH_PRIORITY_QUEUE)
            # 同意，人工执行，不触发自动化脚本执行
            elif opinion == 2:
                next_step = None
                next_status = 4
                next_user = None
                instance.exec_status = 1
            # 移交
            elif opinion == 3:
                next_step = cur_step
                next_status = instance.status
        instance.status = next_status
        instance.cur_step = next_step
        instance.cur_user = next_user
        instance.save()
        # 邮件通知
        workorder_notice(instance)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def feedback(self, request, pk):
        '''
        申请人确认反馈处理结果
        '''
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.status = 4
        opinion = serializer.data["opinion"]
        remark = ''
        if 'remark' in serializer.data:
            remark = serializer.data["remark"]
        if instance.status != 4 and request.user != instance.creator:
            return Response({'detail': ['无权限，流程已更新或您不是申请人']}, status=status.HTTP_400_BAD_REQUEST)
        data = {}
        data['order'] = instance
        data['user'] = request.user
        data['role'] = None
        data['opinion'] = opinion
        data['remark'] = remark
        AuditRecord.objects.create(**data)

        # 已解决
        if opinion == 10:
            next_step = None
            next_status = 5
            next_user = None
        # 未解决回退处理人
        elif opinion == 11:
            steps = AuditStep.objects.filter(workflow=instance.workflow).order_by('order_num')
            next_step = steps.last()
            next_status = 6
            next_user = AuditRecord.objects.filter(order=instance, role=next_step.role).last().user
        instance.status = next_status
        instance.cur_step = next_step
        instance.cur_user = next_user
        instance.save()
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def revoke(self, request, pk):
        '''
        工单撤回
        '''
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if instance.status == 2:
            instance.status = 5
            instance.cur_step = None
            instance.cur_user = None
            instance.save()
            data = {}
            data['order'] = instance
            data['user'] = instance.creator
            data['role'] = None
            data['opinion'] = 11
            data['remark'] = '自己撤回'
            AuditRecord.objects.create(**data)
        else:
            params={}
            params['opinion']=1
            return Response(params)
        return Response(serializer.data)


    @action(methods=['get'], detail=True)
    def auditrecord(self, request, pk):
        '''
        工单审批记录
        '''
        instance = self.get_object()
        records = instance.auditrecord_set.order_by('-id')
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def guestbook(self, request, pk):
        '''
        工单留言
        '''
        instance = self.get_object()
        rets = instance.guestbook_set.order_by('-id')
        serializer = self.get_serializer(rets, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def count_status(self, request):
        '''
        工单状态统计
        '''
        queryset = self.filter_queryset(self.get_queryset())
        data = queryset.values('status').annotate(num=Count('status')).order_by('-num')
        return Response(data)

    @action(methods=['get'], detail=False)
    def count_my_workorder(self, request):
        '''
        我的工单统计
        '''
        user = request.user
        queryset = self.filter_queryset(self.get_queryset())
        data = {}
        data['done'] = len(
            [row.order for row in AuditRecord.objects.filter(user=user).distinct() if row.order.creator != user])
        roles = user.roles.all()
        steps = AuditStep.objects.filter(role__in=roles)
        data['waiting'] = queryset.filter(Q(cur_step__in=steps)).count()
        data['sent'] = queryset.filter(creator=user).count()
        roles = ['super_admin', 'workflow_supervisor', 'workflow_admin']
        is_supervisor = True if user.roles.filter(name__in=roles) else False
        if is_supervisor:
            data['supervise'] = queryset.filter(Q(status=2) | Q(status=3)).count()
            data['all'] = queryset.count()
        return Response(data)

    @action(methods=['post'], detail=False)
    def upload_file(self,request):
        file_obj = request.FILES.get('file')
        save_path =settings.BASE_DIR+'/backend/media/workflow/files/{}'.format(file_obj)
        url_path = "http://www.zeus.com/media/workflow/files/{}".format(file_obj)
        with open(save_path, 'wb') as f:
            for content in file_obj.chunks():
                f.write(content)
        return Response({'name':file_obj.name, "url":url_path})

@api_view(['GET'])
def dingding_audit(request):
        '''
        钉钉审批工单
        '''
        workorder_id = request.GET.get("workorder_id")
        user_id = request.GET.get("user_id")
        opinion = request.GET.get("opinion")
        try:
            opinion = int(opinion)
            workorder = WorkOrder.objects.get(id=workorder_id)
            auditrecord_exits = AuditRecord.objects.filter(order=workorder, user=user_id)
            if auditrecord_exits.exists():
                return Response({"detail": "You have to approved the workorder"})
            AuditRecord.objects.create(
                order=workorder,
                opinion=opinion,
                remark="",
                user=workorder.cur_user,
                role=workorder.cur_step.role
            )
            cur_step = workorder.cur_step
            steps = AuditStep.objects.filter(workflow=workorder.workflow).order_by('order_num')
            next_step = steps.filter(order_num__gt=cur_step.order_num).first()
            next_status = 3
            next_user = None

            if next_step:
                for step in json.loads(workorder.steps):
                    if next_step.id == step["id"]:
                        num=1
                        import random
                        if step["role"]["users"]:
                            num=random.randint(1,len(step["role"]["users"]))
                        next_user = User.objects.get(id=step["role"]["users"][num-1]["id"])
            # 1. 审批人不是工单流程最后审批人
            if cur_step != steps.last():
                # 驳回
                if opinion == 0:
                    next_step = None
                    next_status = 0
                    next_user = None
                # 同意
                else:
                    next_step = next_step
                    next_status = 3
                    next_user = next_user

            # 2. 审批人是工单流程最后审批人
            else:
                # 驳回
                if opinion == 0:
                    next_step = None
                    next_status = 0
                    next_user = None
                    workorder.exec_status = 1
                # 同意
                elif opinion == 1:
                    next_step = None
                    next_status = 4
                    next_user = None
                    workorder_task.apply_async((workorder.id,), queue=settings.HIGH_PRIORITY_QUEUE)
                # 同意，人工执行，不触发自动化脚本执行
                elif opinion == 2:
                    next_step = None
                    next_status = 4
                    next_user = None
                    workorder.exec_status = 1

            workorder.status = next_status
            workorder.cur_step = next_step
            workorder.cur_user = next_user
            workorder.save()

            # 邮件通知
            workorder_notice(workorder)
            return HttpResponse("<strong>工单审批成功！</strong>")
        except Exception as e:
            logger.error(e)
            return HttpResponse("fail")

class AuditRecordViewSet(BaseModelViewSet):
    queryset = AuditRecord.objects.all()
    serializer_class = AuditRecordSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name', 'cname')


class GuestbookViewSet(BaseModelViewSet):
    queryset = Guestbook.objects.all()
    serializer_class = GuestbookSerializer
    ordering_fields = ('id',)
    search_fields = ('content',)


class OpenApiViewSet(BaseModelViewSet):
    queryset = []
    serializer_class = OpenApiSerializer

    @action(methods=['get'], detail=False)
    def dynamic_auditor_demo(self, request):
        '''
        动态审批用户接口demo
        '''
        special = request.query_params.get('special', None)
        n = 2 if special else 3
        queryset = User.objects.all()[:n]
        data = [{'id': row.id, 'username': row.username, 'cname': row.cname} for row in queryset]
        return Response(data)

    @action(methods=['get'], detail=False)
    def dynamic_form_select_demo(self, request):
        '''
        动态表单下拉框demo
        '''
        data = [{'value': 1, 'label': '选项一'}, {'value': 2, 'label': '选项二'}, {'value': 3, 'label': '选项三'}]
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_gitlab_groups(self, request):
        '''
        获取gitlab项目组列表
        '''
        rets = get_gitlab_groups()
        data = [{'value': row.id, 'label': row.full_path} for row in rets]
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_gitlab_group_names(self, request):
        '''
        获取gitlab项目组名称列表
        '''
        rets = get_gitlab_groups()
        data = [{'value': row.full_path, 'label': row.full_path} for row in rets]
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_gitlab_projects(self, request):
        '''
        获取gitlab项目列表
        '''
        group_id = request.query_params.get('group_id', 0)
        if not group_id: return Response({'detail': ['group_id参数不能为空']}, status=status.HTTP_400_BAD_REQUEST)
        rets = get_gitlab_projects(group_id)
        data = [{'value': row.id, 'label': row.http_url_to_repo} for row in rets]
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_gitlab_group_auditors(self, request):
        '''
        获取gitlab项目组审批人
        '''
        data = []
        group_id = request.query_params.get('group_id', 0)
        if group_id:
            auditors = get_gitlab_group_auditors(int(group_id))
            users = [row.username for row in auditors]
            data = [{'id': row.id, 'username': row.username, 'cname': row.cname} for row in
                    User.objects.filter(username__in=users)]
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_strees(self, request):
        '''
        获取服务树节点
        '''
        deep = request.query_params.get('deep', settings.MAXDEEP)
        ishostpool = request.query_params.get('ishostpool', 1)
        exclude2 = request.query_params.get('exclude2', "")
        isone = request.query_params.get('isone', 0)
        rets = get_strees(isone=int(isone),deep=int(deep), ishostpool=int(ishostpool),exclude2=exclude2)
        data = [{'value': row['id'], 'label': row['path']} for row in rets]
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_stree_roles(self, request):
        '''
        获取服务树角色
        '''
        rets = get_stree_roles()

        data = []
        for row in rets:
            if row.name == 'rd':
                data.append({'value': row.id, 'label': row.cname + ":具有查看树节点权限"})
            elif row.name == 'rd_admin':
                data.append({'value': row.id, 'label': row.cname + ":具有查看树节点权限，同时还有审批RD权限"})
            elif row.name == 'op':
                data.append({'value': row.id, 'label': row.cname + ":具有查看、新建和编辑树节点权限"})
            elif row.name == 'op_admin':
                data.append({'value': row.id, 'label': row.cname + ":具有查看、新建、编辑和拖拽树节点权限，同时还有审批OP权限"})
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_stree_auditors(self, request):
        '''
        获取服务树节点审批人
        '''
        rets = get_stree_auditors()
        data = [{'value': row.id, 'label': row.cname} for row in rets]
        return Response(data)

    @action(methods=['get'], detail=False)
    def get_cicd_mods(self, request):
        '''
        获取cicd模块列表
        '''
        rets = get_cicd_mods()
        data = [{'value': row.id, 'label': row.name} for row in rets]
        return Response(data)
