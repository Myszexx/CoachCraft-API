# from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from players.models import Players, Ratings
from players.serializers import PlayersSerializer, RatingsSerializer


# Create your views here.


class PlayerMVS(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer

class RatingsList(generics.ListCreateAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


# class PlayerRatings(generics.RetrieveAPIView):
#     queryset = Ratings.objects.all()
#     serializer_class = RatingsSerializer
#     lookup_field = 'player_id'


# class PlayerRating(generics.GenericAPIView):
#     serializer_class = RatingsSerializer
