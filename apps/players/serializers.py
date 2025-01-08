from rest_framework import serializers

from apps.players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'country', 'birthdate']

