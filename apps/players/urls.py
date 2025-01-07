from django.contrib import admin
from django.urls import path, include

from apps.players.views import player_list, player_details

urlpatterns = [
    path('', player_list, name='players'),
    path('<int:pk>', player_details, name='player_details'),
]