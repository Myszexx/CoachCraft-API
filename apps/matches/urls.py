from django.contrib import admin
from django.urls import path, include

from apps.matches.views import MatchListV, MatchDetailV, MatchSquadV, MatchEventsV

urlpatterns = [
    path('', MatchListV.as_view(), name='matches_list'),
    path('details/<int:pk>',MatchDetailV.as_view(), name='match_details'),
    path('squad/',MatchSquadV.as_view(), name='match_squad'),
    path('events/', MatchEventsV.as_view(), name='match_events'),
]