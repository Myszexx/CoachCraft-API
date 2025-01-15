from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from apps.matches.models import Matches, MatchSquad
from apps.matches.serializers import MatchesSerializer, MatchSquadSerializer



class MatchListV(generics.ListCreateAPIView):
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer

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