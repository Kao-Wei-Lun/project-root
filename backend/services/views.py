from rest_framework import viewsets
from .models import Service, Consultant, Feedback
from .serializers import ServiceSerializer, ConsultantSerializer, FeedbackSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'  # 指定使用 slug 作為查找欄位

class ConsultantViewSet(viewsets.ModelViewSet):
    """
    諮詢師 API：支援 GET、POST、PUT、PATCH、DELETE 等操作
    """
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    """
    回饋 API：依 created_at 降序排列，最新的在最前面
    """
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer