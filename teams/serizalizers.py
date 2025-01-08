from rest_framework import serializers


from teams.models import Teams, PlayersAffilations


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class PlayersAffilationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersAffilations
        fields = '__all__'