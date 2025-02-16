from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from apps.teams.models import Teams, PlayersAffilations, TeamSquad


class PlayersAffilationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersAffilations
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class TeamDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSquad
        fields = ["player_id","team_id"]

class UserTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'