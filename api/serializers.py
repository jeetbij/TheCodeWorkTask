from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Todo

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['id', 'created_at']