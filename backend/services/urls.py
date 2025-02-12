from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ConsultantViewSet, FeedbackViewSet

router = DefaultRouter()
# 此處使用 basename 明確指定，避免自動推導可能造成的問題
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'consultants', ConsultantViewSet, basename='consultant')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    # 將 router.urls 包含在 api/ 下
    path('api/', include(router.urls)),
]
