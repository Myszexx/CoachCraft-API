from rest_framework import serializers
from matches.models import Matches, MatchSquad, MatchEvents

class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'

class MatchSquadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchSquad
        fields = '__all__'

class MatchEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchEvents
        fields = '__all__'
