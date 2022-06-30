# -*- coding: utf-8 -*-
#author Jack qq:774428957
from rest_framework import serializers
from djcelery.models import PeriodicTask, CrontabSchedule, IntervalSchedule
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class IntervalScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntervalSchedule
        fields = '__all__'

class CrontabScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CrontabSchedule
        fields = '__all__'

class PeriodicTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodicTask
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'