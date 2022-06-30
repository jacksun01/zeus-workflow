#coding=utf8
#author Jack qq:774428957
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from modellog.mixins import LoggingViewSetMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models.query import QuerySet
import logging
from cicd.models import *
from stree.models import *

logger = logging.getLogger('views')

class DefaultPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 1000

class BaseModelNoListViewSet(LoggingViewSetMixin, viewsets.ModelViewSet):
    pagination_class = DefaultPagination

    @action(methods=['get'], detail=False)
    def get_table_info(self, request):
        '''
        获取表字段名和过滤选项
        '''
        data = {}
        if hasattr(self.queryset.model(), 'get_table_info'):
            data = self.queryset.model().get_table_info()

        return Response(data)

class BaseModelViewSet(LoggingViewSetMixin, viewsets.ModelViewSet):
    pagination_class = DefaultPagination
    '''
        list排序 需要重新定义排序情况
    '''
    def list(self, request):
        ordering = request.query_params.get('ordering', '')
        ordering = ordering.replace('+', '').strip()
        if ordering:
            if self.serializer_class is None:
                queryset = self.filter_queryset(self.get_serializer_class().Meta.model.objects.order_by(ordering))
            else:
                queryset = self.filter_queryset(self.serializer_class.Meta.model.objects.order_by(ordering))
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def get_table_info(self, request):
        '''
        获取表字段名和过滤选项
        '''
        data = {}
        if hasattr(self.get_queryset().model(), 'get_table_info'):
            data = self.get_queryset().model().get_table_info()

        return Response(data)

class BaseGenericViewSet(LoggingViewSetMixin, viewsets.GenericViewSet):
    pagination_class = DefaultPagination
