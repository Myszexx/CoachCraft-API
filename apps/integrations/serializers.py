from rest_framework import serializers
from apps.integrations.models import LinkedList, ZPNs, Leagues


class ZPNsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZPNs
        fields = ('url', 'name')

class LeaguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = ('zpn_id', 'url', 'name', 'season')