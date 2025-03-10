from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_206_PARTIAL_CONTENT

from apps.events.utils import get_current_season
from apps.integrations.models import ZPNs, Leagues
# from API.integrations.PFScrapper.grcp_client import GRPCClient as grcp
from apps.integrations.serializers import ZPNsSerializer, LeaguesSerializer


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

class NinetyMinsListV(generics.CreateAPIView):
    permission_classes = [AllowAny]


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
                    zpn_id = ZPNs.objects.filter(name=item['zpn']).first().id
                    season = item['season'] if item['season'] else get_current_season()
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