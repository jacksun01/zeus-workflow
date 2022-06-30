# -*- coding:utf-8 -*-
#author Jack qq:774428957
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from utils.base_view import BaseModelViewSet, BaseGenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import LogsEntry
from .serializers import LogsEntrySerializer, ContentTypeSerializer
from .filters import LogsEntryFilter


class LogsEntryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, BaseGenericViewSet):
    queryset = LogsEntry.objects.order_by('-id')
    serializer_class = LogsEntrySerializer
    ordering_fields = ('id', 'user')
    search_fields = ('message','user__username')
    filterset_class = LogsEntryFilter

    @action(methods=['get'], detail=False)
    def get_table_info(self, request):
        '''
        获取表字段名和过滤选项
        '''
        return Response(self.queryset.model().get_table_info())

class ContentTypeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ContentType.objects.order_by('-id')
    serializer_class = ContentTypeSerializer

# class LogsEntryDetailApiView(generics.RetrieveAPIView):
#     """日志详情API"""
#     queryset = LogsEntry.objects.all()
#     serializer_class = LogsEntrySerializer
#     # 权限控制
#     permission_classes = (IsAuthenticated,)
#
#
# class ModelLogsEntryListAPIView(generics.ListAPIView):
#     """
#     获取日志列表api
#     """
#     queryset = LogsEntry.objects.all()
#     serializer_class = LogsEntrySerializer
#     # 权限控制
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         # 第1步：先获取到app和model的字符串
#         app = self.kwargs['app']
#         model = self.kwargs['model']
#
#         # 第2步：获取到Model的content_type
#         content_type = get_object_or_404(ContentType, app_label=app, model=model)
#
#         # 第3步：获取数据
#         objects_list = LogsEntry.objects.filter(content_type=content_type).order_by('-time_added')
#
#         # 第4步：返回数据
#         return objects_list
#
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#
# class ObjectLogsListDetailApiView(generics.ListAPIView):
#     """
#     获取model某个对象的历史记录列表
#     """
#     serializer_class = LogsEntrySerializer
#     # 权限控制
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         # 第1步：先获取到app和model的字符串，pk
#         app = self.kwargs['app']
#         model = self.kwargs['model']
#         pk = self.kwargs['pk']
#
#         # 第2步：获取到Model的content_type
#         content_type = get_object_or_404(ContentType, app_label=app, model=model)
#
#         # 第3步：获取数据
#         objects_list = LogsEntry.objects.filter(content_type=content_type,
#                                                 object_id=pk).order_by('-time_added')
#
#         # 第4步：返回数据
#         return objects_list
#
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
