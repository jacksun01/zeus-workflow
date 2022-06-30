# -*- coding: utf-8 -*-
#author Jack qq:774428957
import os
from django.apps import AppConfig

app_name = os.path.basename(os.path.dirname(__file__))

class AppConfig(AppConfig):
    name = app_name
    verbose_name = '工单系统'
