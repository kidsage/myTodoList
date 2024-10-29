from rest_framework import serializers
from .models import List
from api.cards.serializers import CardSerializer


class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = '__all__'
