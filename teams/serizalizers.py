from rest_framework import serializers


from teams.models import Teams, PlayersAffilations, Trainings


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class PlayersAffilationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersAffilations
        fields = '__all__'

class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainings
        fields = '__all__'