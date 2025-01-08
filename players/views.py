# from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from players.models import Player, Ratings
from players.serializers import PlayerSerializer, RatingsSerializer


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


# class PlayerRating(generics.GenericAPIView):
#     serializer_class = RatingsSerializer
#
#     def get_queryset(self, data):
#         player_id = data.get('player_id')
#         match_id = data.get('match_id')
#         training_id = data.get('training_id')
#
#         if not player_id or not (match_id or training_id):
#             return Ratings.objects.none()
#
#         return Ratings.objects.filter(player_id=player_id,
#                                       match_id=match_id,
#                                       training_id=training_id)
#
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset(request.data)
#         if not queryset.exists():
#             return Response(
#                 {"Error": "Rating not found for the given player, match, or training"},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = self.get_serializer(queryset.first())
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, *args, **kwargs):
#         queryset = self.get_queryset(request.data)
#         if not queryset.exists():
#             return Response(
#                 {"Error": "Rating not found for the given player, match, or training"},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         instance = queryset.first()
#         serializer = self.get_serializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, *args, **kwargs):
#         queryset = self.get_queryset(request.data)
#         if not queryset.exists():
#             return Response(
#                 {"Error": "Rating not found for the given player, match, or training"},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         instance = queryset.first()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
