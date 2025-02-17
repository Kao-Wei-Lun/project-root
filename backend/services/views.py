from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
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
    parser_classes = (JSONParser,MultiPartParser, FormParser)
    
    # 如果希望所有更新都視為部分更新，可以覆寫 update() 方法：
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # 強制部分更新
        return super().update(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        service = self.request.query_params.get('service')
        if service:
            # 篩選 service_items 包含指定服務的記錄（簡單範例，不夠精確）
            queryset = queryset.filter(service_items__icontains=service)
        return queryset
    
class FeedbackViewSet(viewsets.ModelViewSet):
    """
    回饋 API：依 created_at 降序排列，最新的在最前面
    """
    queryset = Feedback.objects.all().order_by('order')  # 如需順序調整，根據 order 排序
    serializer_class = FeedbackSerializer
    # Feedback 一般不涉及檔案上傳，故不需要 parser_classes
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)