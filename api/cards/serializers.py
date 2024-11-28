from rest_framework import serializers
from .models import Card
from api.comments.serializers import CommentSerializer
from api.attachments.serializers import AttachmentSerializer


class CardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = '__all__'
