# -*- coding: utf-8 -*-
#author Jack qq:774428957
from django.db import models
from utils.util import deal_fields_Table

class BaseModel(models.Model):
    '''
       基础表(抽象类)
    '''
    name = models.CharField(verbose_name='名称', help_text='名称', max_length=128, default='')
    cname = models.CharField(verbose_name='中文名称', help_text='中文名称', max_length=128, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(verbose_name='更新时间', help_text='更新时间', auto_now=True, null=True, blank=True)
    remark = models.TextField(verbose_name='备注', help_text='备注', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['-id']

    def get_fields(self):
        """
        获取字段信息
        """
        field_dict = {}
        for field in self._meta.fields:
            field_dict[field.name] = field.verbose_name
        return field_dict

    def get_table_info(self):
        """
        获取table表
        """
        data = deal_fields_Table(self._meta.fields, True, True, 2, None, None, None)
        return data

class BaseTimeModel(models.Model):
    '''
       基础表(抽象类)
    '''
    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(verbose_name='更新时间', help_text='更新时间', auto_now=True, null=True, blank=True)
    remark = models.TextField(verbose_name='备注', help_text='备注', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-id']

    def get_table_info(self):
        """
        获取table表
        """
        data = deal_fields_Table(self._meta.fields, True, True, 2, None, None, None)
        return data