from rest_framework import serializers
from apps.events.models import Matches, MatchSquad, MatchEvents, MatchEventTypes, Trainings, CustomEvents


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

class MatchEventTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchEventTypes
        fields = '__all__'

class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainings
        fields = '__all__'

class CustomEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomEvents
        fields = '__all__'

