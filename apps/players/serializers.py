from rest_framework import serializers
from apps.players.models import Player
from .utils import calculate_age  # Import the function


class PlayerSerializer(serializers.ModelSerializer):
    player_age = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = '__all__'
        # exclude #jezeli jest all

    def get_player_age(self, obj):
        return calculate_age(obj.birthdate)
