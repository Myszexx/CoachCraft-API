from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from players.models import Player, Ratings
from players.serializers import PlayerSerializer, RatingsSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.


# Create your views here.
class PlayerListAV(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetailAV(APIView):
    def get(self,request,pk):
        try:
            player = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response({"Error":"Player not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def put(self,request,pk):
        try:
            player = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response({"Error":"Player not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,pk):
        try:
            player = Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            return Response({"Error":"Player not found"},status=status.HTTP_404_NOT_FOUND)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RatingsList(generics.ListCreateAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class PlayerRatings(generics.RetrieveAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    lookup_field = 'player_id'

    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

#TODO Dodac obsluge wybierania ratingu danego zawodnika z danego meczu/treningu