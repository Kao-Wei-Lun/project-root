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

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'  # 或指定 ['id', 'user', 'comment', 'created_at']