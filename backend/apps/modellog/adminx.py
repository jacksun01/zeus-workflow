# -*- coding: utf-8 -*-
#author Jack qq:774428957
import xadmin
from .models import LogsEntry

class LogsEntryAdmin(object):
    list_display = ["time_added", "user", "object_repr", "action_flag", "message"]

xadmin.site.register(LogsEntry, LogsEntryAdmin)