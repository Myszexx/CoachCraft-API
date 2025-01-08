from django.contrib import admin
from django.urls import path, include

from players.views import PlayerListAV, PlayerDetailAV, RatingsList

# from players.views import player_list, player_details

urlpatterns = [
    path('', PlayerListAV.as_view(), name='players'),
    path('<int:pk>', PlayerDetailAV.as_view(), name='player_details'),
    path('ratings/', RatingsList.as_view(), name='reviews_list'),
    path('<int:pk>/ratings/', RatingsList.as_view(), name='player_review'),
]