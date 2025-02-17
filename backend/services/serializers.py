# services/serializers.py
from rest_framework import serializers
from .models import Service, Consultant, Feedback

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = '__all__'  # 或指定 ['id', 'name', 'description', 'image']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            # order 欄位也可設定 required=False，方便部分更新
            'order': {'required': False},
        }

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'  # 或指定 ['id', 'user', 'comment', 'created_at']

class PublicConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ['id', 'name', 'description', 'image', 'order']
        extra_kwargs = {
            'user': {'required': False},
            'comment': {'required': False},
            'order': {'required': False},
        }