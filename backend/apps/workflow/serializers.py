# -*- coding: utf-8 -*-
#author Jack qq:774428957
from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.serializers import RoleSerializer
from .models import *

User = get_user_model()

class WorkFlowGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkFlowGroup
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        workflow_instances = WorkFlow.objects.filter(group=instance)
        serializer = WorkFlowSerializer(workflow_instances, many=True)
        ret['workflow'] = serializer.data
        return ret

class FormFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormField
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        workflow = validated_data['workflow']
        last_instance = workflow.formfield_set.order_by('order_num').last()
        if last_instance: instance.order_num = last_instance.order_num + 1
        instance.save()
        return instance

class AuditStepSerializer(serializers.ModelSerializer):

    role = serializers.PrimaryKeyRelatedField(label="角色", help_text="角色", required=False,queryset=Role.objects.all())
    class Meta:
        model = AuditStep
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        workflow = validated_data['workflow']
        last_instance = workflow.auditstep_set.order_by('order_num').last()
        if last_instance: instance.order_num = last_instance.order_num + 1
        instance.save()
        return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        role_instance = instance.role
        role_serializer = RoleSerializer(role_instance)
        ret['role'] = role_serializer.data
        return ret


class WorkFlowSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkFlow
        read_only_fields = ('num', )
        fields = '__all__'

    # def create(self, validated_data):
    #     instance = super().create(validated_data=validated_data)
    #     defalut_field = [
    #         {'workflow': instance, 'type': 'input', 'field':'title', 'title':'标题', 'value':None, 'props':None, 'order_num':1},
    #         {'workflow': instance, 'type': 'input', 'field':'test', 'title':'测试', 'value':None, 'props':None, 'order_num':2},
    #     ]
    #     for d in defalut_field:
    #         FormField.objects.create(**d)
    #     instance.save()
    #     return instance

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        step_instances = AuditStep.objects.filter(workflow=instance).order_by('order_num')
        ret['steps'] = '->'.join([row.role.cname for row in step_instances])
        ret['group_cname'] = None if not instance.group else instance.group.cname
        ret['is_automatic'] = True if instance.script else False
        return ret

class WorkOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOrder
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['cur_role_detail'] = ret['cur_role_detail'] = ret['creator_detail'] = None
        if instance.cur_user: ret['cur_user_detail'] = {'username':instance.cur_user.username, 'email':instance.cur_user.email, 'cname':instance.cur_user.cname}
        if instance.cur_step: ret['cur_role_detail'] = {'name':instance.cur_step.role.name, 'cname':instance.cur_step.role.cname}
        if instance.creator: ret['creator_detail'] = {'username': instance.creator.username,'email': instance.creator.email, 'cname': instance.creator.cname}
        ret['has_script'] = False
        if hasattr(instance.workflow, 'script'):
            if instance.workflow.script: ret['has_script'] = True
        return ret

class WorkOrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOrder
        exclude = ('formfields','data', 'exec_log', 'file_info')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['cur_role_detail'] = ret['cur_role_detail'] = ret['creator_detail'] = None
        if instance.cur_user: ret['cur_user_detail'] = {'username':instance.cur_user.username, 'email':instance.cur_user.email, 'cname':instance.cur_user.cname}
        if instance.cur_step: ret['cur_role_detail'] = {'name':instance.cur_step.role.name, 'cname':instance.cur_step.role.cname}
        if instance.creator: ret['creator_detail'] = {'username': instance.creator.username,'email': instance.creator.email, 'cname': instance.creator.cname}
        ret['has_script'] = False
        if hasattr(instance.workflow, 'script'):
            if instance.workflow.script: ret['has_script'] = True
        return ret


class AuditSerializer(serializers.ModelSerializer):
    opinion = serializers.ChoiceField(label='处理意见', help_text='处理意见', choices=AuditRecord.OPINION[:-2])
    next_user = serializers.PrimaryKeyRelatedField(label="用户", help_text="用户", required=False, queryset=User.objects.all())

    class Meta:
        model = AuditRecord
        read_only_fields = ('order', 'user', 'role')
        fields = '__all__'


class AuditRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuditRecord
        read_only_fields = ('order', 'user', 'role')
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['user_detail'] = ret['role_detail'] = None
        if instance.user: ret['user_detail'] = {'username': instance.user.username, 'cname': instance.user.cname, 'id': instance.user.id}
        # if getattr(instance, 'role', None) is not None: ret['role'] = {'name': instance.role.name, 'cname': instance.role.cname, 'id': instance.role.id}
        if instance.role: ret['role_detail'] = {'name': instance.role.name, 'cname': instance.role.cname, 'id': instance.role.id}
        return ret

class FeedbackSerializer(serializers.ModelSerializer):
    opinion = serializers.ChoiceField(label='反馈意见', help_text='处理意见', choices=AuditRecord.OPINION[-2:])
    class Meta:
        model = AuditRecord
        read_only_fields = ('order', 'user', 'role')
        fields = '__all__'

class RevokeSerializer(serializers.ModelSerializer):
    opinion = serializers.ChoiceField(label='反馈意见', help_text='处理意见', choices=AuditRecord.OPINION[-2:])
    class Meta:
        model = AuditRecord
        read_only_fields = ('order', 'user', 'role')
        fields = '__all__'

class CreateWorkOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOrder
        fields = ('workflow', 'data', 'cur_user', 'formfields', 'file_info')

class OpenApiSerializer(serializers.Serializer):

    pass

class GuestbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestbook
        fields = '__all__'
