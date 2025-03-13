from django.shortcuts import render
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

# class ZPNsListV(generics.RetrieveAPIView):
#     serializer_class = LinkedListSerializer
#
#     def get(self, request):
#         data = grcp().get_data('/ligireg.html')
#         if not LinkedListSerializer(data).is_valid():
#             return Response(status=HTTP_204_NO_CONTENT)
#
#         return Response(data, status=HTTP_200_OK)

class NinetyMinsListV(generics.ListCreateAPIView):
    permission_classes = [AllowAny]


    def get(self, request, *args, **kwargs):
        print(**kwargs)
        type = request.query_params.get('type')
        filter = request.query_params.get('filter')
        queryset = None
        match type:
            case 'ZPNs':
                queryset = ZPNs.objects.all()
                serializer = ZPNsSerializer(queryset, many=True)
            case 'Leagues':
                queryset = Leagues.objects.filter(zpn__name__contains=filter)
                serializer = LeaguesSerializer(queryset, many=True)
            case 'Tables':
                queryset = Table.objects.filter(league__table__name__contains=filter)
                serializer = TableSerializer(queryset, many=True)
            case 'Fixtures':
                queryset = Fixtures.objects.filter(Q(home_team__icontains=filter)|Q(away_team__icontains=filter))
                serializer = FixturesSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data['data']
        type = request.data['type']
        is_good = True

        match type:
            case 'ZPNs':

                for item in data:
                    print(item)
                    serializer = ZPNsSerializer(data=item)
                    if serializer.is_valid():
                        print('valid')
                        serializer.save()
                    else:
                        is_good = False
                if not is_good:
                    return Response(status=HTTP_206_PARTIAL_CONTENT)
                return Response(status=HTTP_200_OK)
            case 'Leagues':
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
            case 'Tables':
                for item in data:
                    league_id = Leagues.objects.filter(name=item['league']).first().id
                    table = {
                        'league_id': league_id,
                        'team_name': item['name'],
                        'team_url': item['url'],
                        'matches': item['wins']+item['draws']+item['loses'],
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
            case 'Fixtures':
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