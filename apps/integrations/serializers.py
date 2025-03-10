from rest_framework import serializers
from apps.integrations.models import LinkedList, ZPNs, Leagues, Table, Fixtures


class ZPNsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZPNs
        fields = ('url', 'name')

class LeaguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = ('zpn_id', 'url', 'name', 'season')

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('league_id', 'team_name', 'team_url', 'matches', 'wins', 'draws', 'losses', 'goals_scored', 'goals_conceded', 'points', 'position')

class FixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixtures
        fields = ('league_id', 'home_team', 'away_team', 'date', 'time')