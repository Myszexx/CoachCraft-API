from rest_framework import serializers
from players.models import Players, Ratings
from .utils import calculate_age, is_youth_player  # Import the function


class PlayersSerializer(serializers.ModelSerializer):
    player_age = serializers.SerializerMethodField()
    is_youngster = serializers.SerializerMethodField()

    class Meta:
        model = Players
        fields = '__all__'
        # exclude #jezeli jest all

    def get_player_age(self, obj):
        return calculate_age(obj.birthdate)

    def get_is_youngster(self, obj):
        return is_youth_player(obj.birthdate)

class RatingsSerializer(serializers.ModelSerializer):
    rating_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Ratings
        fields = '__all__'