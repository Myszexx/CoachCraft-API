from django.core.serializers import serialize
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from apps.events.models import Matches, MatchSquad
from apps.events.serializers import MatchesSerializer, MatchSquadSerializer, TrainingsSerializer, CustomEventsSerializer


class AllEventsListV(generics.ListAPIView):

    def get_matches(self,team_id):
        matches = Matches.objects.filter(team_id=team_id)
        serializer = MatchesSerializer(matches, many=True)
        if serializer.is_valid():
            return matches
        return {'error': 'trainings not resolved', 'status': 400}

    def get_trainings(self,team_id):
        trainings = Matches.objects.filter(team_id=team_id)
        serializer = TrainingsSerializer(trainings, many=True)
        if serializer.is_valid():
            return trainings
        return {'error': 'trainings not resolved', 'status': 400}

    def get_custom_events(self,team_id):
        custom_events = Matches.objects.filter(team_id=team_id)
        serializer = CustomEventsSerializer(custom_events, many=True)
        if serializer.is_valid():
            return custom_events
        return {'error': 'trainings not resolved', 'status': 400}

    def get(self, request, *args, **kwargs):
        team_id = kwargs.get('pk')
        data = {
            'customs': self.get_custom_events(team_id),
            'matches': self.get_matches(team_id),
            'trainings': self.get_trainings(team_id)
        }
        return Response(data)

class MatchListV(generics.ListCreateAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer
    filter_backends = [DjangoFilterBackend]
    filter_backends = ['team_id']

class MatchDetailV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer

class MatchSquadV(generics.RetrieveAPIView):
    queryset = MatchSquad.objects.all()
    serializer_class = MatchSquadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['match_id',]#'team_id']

class MatchEventsV(generics.ListCreateAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['match_id']

class TrainingsListV(generics.ListCreateAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['team_id']

class TrainingsDetailV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer

class CustomEventsListV(generics.ListCreateAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['team_id']

class CustomEventsDetailV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['team_id']