# -*- coding: utf-8 -*-
#author Jack qq:774428957
import xadmin
from .models import *

class WorkFlowGroupAdmin(object):
    list_display = ["name", "cname", "create_time"]
    search_fields = ['name', "cname"]

class WorkFlowAdmin(object):
    list_display = ["id", "name", "cname", "description", "is_active", "create_time"]
    search_fields = ['name', "cname"]

class AuditStepAdmin(object):
    list_display = ["workflow", "role", "order_num"]

class FormFieldAdmin(object):
    list_display = ["workflow", "type", "field", "title", "value", "order_num"]

class WorkOrderAdmin(object):
    list_display = ["id", "name", "cname", "description", "create_time"]
    search_fields = ["id", "name", "cname"]
    list_filter = ['id', 'exec_status', 'status', 'workflow']

class AuditRecordAdmin(object):
    list_display = ["create_time"]

xadmin.site.register(WorkFlowGroup, WorkFlowGroupAdmin)
xadmin.site.register(WorkFlow, WorkFlowAdmin)
xadmin.site.register(AuditStep, AuditStepAdmin)
xadmin.site.register(FormField, FormFieldAdmin)
xadmin.site.register(WorkOrder, WorkOrderAdmin)
xadmin.site.register(AuditRecord, AuditRecordAdmin)