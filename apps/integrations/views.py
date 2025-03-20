from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_206_PARTIAL_CONTENT
from django.db.models import Q

from apps.events.utils import get_current_season
from apps.integrations.models import ZPNs, Leagues, Table, Fixtures
# from API.integrations.PFScrapper.grcp_client import GRPCClient as grcp
from apps.integrations.serializers import ZPNsSerializer, LeaguesSerializer, TableSerializer, FixturesSerializer


# Create your views here.

class ZPNsListV(generics.ListCreateAPIView):
    queryset = ZPNs.objects.all()
    serializer_class = ZPNsSerializer
    permission_classes = [AllowAny]

class LeaguesListV(generics.ListCreateAPIView):
    queryset = Leagues.objects.all()
    serializer_class = LeaguesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Leagues.objects.all()
        zpn = self.request.query_params.get('zpn', None)
        if zpn is not None:
            queryset = queryset.filter(zpn__name__contains=filter)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data['data']
        is_good = True
        for item in data:
            print(item)
            zpn_id = ZPNs.objects.filter(name=item['zpn']).first().id
            season = item['season'] if 'season' in item.keys() else get_current_season()
            league = {
                'name': item['name'],
                'url': item['url'],
                'zpn_id': zpn_id,
                'season': season
            }
            serializer = LeaguesSerializer(data=item)
            if serializer.is_valid():
                Leagues.objects.update_or_create(**league)
            else:
                is_good = False

        if not is_good:
            return Response(status=HTTP_206_PARTIAL_CONTENT)
        return Response(status=HTTP_200_OK)



class TableListV(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Table.objects.all()
        league = self.request.query_params.get('league', None)
        if league is not None:
            queryset = queryset.filter(league__table__name__contains=filter)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data['data']
        is_good = True
        for item in data:
            league_id = Leagues.objects.filter(name=item['league']).first().id
            table = {
                'league_id': league_id,
                'team_name': item['name'],
                'team_url': item['url'],
                'matches': item['wins'] + item['draws'] + item['loses'],
                'wins': item['wins'],
                'draws': item['draws'],
                'losses': item['loses'],
                'goals_scored': item['goals_shot'],
                'goals_conceded': item['goals_conceded'],
                'points': item['points'],
                'position': item['standing']
            }
            serializer = TableSerializer(data=table)
            if serializer.is_valid():
                Table.objects.update_or_create(**table)
            else:
                is_good = False

        if not is_good:
            return Response(status=HTTP_206_PARTIAL_CONTENT)
        return Response(status=HTTP_200_OK)

class FixturesListV(generics.ListCreateAPIView):
    queryset = Fixtures.objects.all()
    serializer_class = FixturesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Fixtures.objects.all()
        team = self.request.query_params.get('team', None)
        if team is not None:
            queryset = queryset.filter(Q(home_team__icontains=filter)|Q(away_team__icontains=filter))
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data['data']
        is_good = True
        for item in data:
                    league_id = Leagues.objects.filter(name=item['league']).first().id
                    fixture = {
                        'league_id': league_id,
                        'home_team': item['home_team'],
                        'away_team': item['away_team'],
                        'date': item['date'],
                        'time': item['time']
                    }
                    serializer = FixturesSerializer(data=fixture)
                    if serializer.is_valid():
                        Fixtures.objects.update_or_create(**fixture)
                    else:
                        is_good = False

        if not is_good:
            return Response(status=HTTP_206_PARTIAL_CONTENT)
        return Response(status=HTTP_200_OK)

