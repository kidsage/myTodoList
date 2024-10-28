from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)  # owner의 username 필드를 가져옴

    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'owner', 'owner_name']
        read_only_fields = ['owner_name']
