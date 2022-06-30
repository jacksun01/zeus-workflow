#author Jack qq:774428957
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'periodictasks', PeriodicTaskViewSet)
router.register(r'intervals', IntervalScheduleViewSet)
router.register(r'crontabs', CrontabScheduleViewSet)
urlpatterns = router.urls
