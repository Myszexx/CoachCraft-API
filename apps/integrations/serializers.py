from rest_framework import serializers
from apps.integrations.models import LinkedList


class LinkedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedList
        fields = ('url', 'to')