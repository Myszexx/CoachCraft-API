from django.contrib import admin
from django.urls import path, include

from apps.players.views import PlayerListAV, PlayerDetailAV

# from apps.players.views import player_list, player_details

urlpatterns = [
    path('', PlayerListAV.as_view(), name='players'),
    path('<int:pk>', PlayerDetailAV.as_view(), name='player_details'),
]