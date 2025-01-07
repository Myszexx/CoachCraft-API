from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.players.models import Player
from apps.players.serializers import PlayerSerializer


# Create your views here.
@api_view(['GET','POST'])
def player_list(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def player_details(request, pk):
    if request.method == 'GET':
        player = Player.objects.get(pk=pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
    elif request.method == 'PUT':
        player = Player.objects.get(pk=pk)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        player = Player.objects.get(pk=pk)
        player.delete()
        return Response(status=204)