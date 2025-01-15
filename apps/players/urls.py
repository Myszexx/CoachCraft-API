from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.players.views import RatingsList, PlayerMVS, RatingsCreate

# from players.views import player_list, player_details

routers = DefaultRouter()
routers.register('players', PlayerMVS)
urlpatterns = [
    path('', include(routers.urls)),
    # path('', PlayerListAV.as_view(), name='players'),
    # path('<int:pk>', PlayerDetailAV.as_view(), name='player_details'),
    path('ratings/', RatingsList.as_view(), name='reviews_list'),
    path('rating-create/', RatingsCreate.as_view(), name='review_create')
    # path('<int:pk>/ratings/', PlayerRating.as_view(), name='player_review'),
]