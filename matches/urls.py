from django.contrib import admin
from django.urls import path, include

from matches.views import MatchListV, MatchDetailV, MatchSquadV

urlpatterns = [
    path('', MatchListV.as_view(), name='matches_list'),
    path('details/<int:pk>',MatchDetailV.as_view(), name='match_details'),
    path('squad/',MatchSquadV.as_view(), name='match_squad'),
]