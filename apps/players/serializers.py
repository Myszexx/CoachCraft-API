from rest_framework import serializers

from apps.players.models import Player


class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    country = serializers.CharField()
    birthdate = serializers.DateField()

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.country = validated_data.get('country', instance.country)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
