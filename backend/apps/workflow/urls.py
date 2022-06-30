#author Jack qq:774428957
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'auditsteps', AuditStepViewSet)
router.register(r'formfields', FormFieldViewSet)
router.register(r'workflowgroups', WorkFlowGroupViewSet)
router.register(r'workflows', WorkFlowViewSet)
router.register(r'workorders', WorkOrderViewSet)
router.register(r'auditrecords', AuditRecordViewSet)
router.register(r'guestbooks', GuestbookViewSet)
router.register(r'openapis', OpenApiViewSet,base_name='openapi')

urlpatterns = router.urls
