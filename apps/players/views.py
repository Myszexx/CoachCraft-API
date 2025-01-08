from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.players.models import Player
from apps.players.serializers import PlayerSerializer
from rest_framework import status


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



# @api_view(['GET','PUT','DELETE'])
# def player_details(request, pk):
#     try:
#         player = Player.objects.get(pk=pk)
#     except Player.DoesNotExist:
#         return Response({"Error":"Player not found"},status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = PlayerSerializer(player)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PlayerSerializer(player, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == 'DELETE':
#         player.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)