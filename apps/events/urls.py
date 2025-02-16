from django.contrib import admin
from django.urls import path, include

from apps.events.views import MatchListV, MatchDetailV, MatchSquadV, MatchEventsV, TrainingsListV, TrainingsDetailV, \
    CustomEventsListV, CustomEventsDetailV, AllEventsListV

urlpatterns = [
    #EVENTS CORE section
    path('all_eventes/<int:pk>', AllEventsListV.as_view(), name='all_events_list'),
    #MATCHES section
    path('matches/', MatchListV.as_view(), name='matches_list'),
    path('matches/details/<int:pk>',MatchDetailV.as_view(), name='match_details'),
    path('matches/<int:pk>/squad/',MatchSquadV.as_view(), name='match_squad'),
    path('matches/<int:pk>/events/', MatchEventsV.as_view(), name='match_events'),
    #TRAINING section
    path('trainings/', TrainingsListV.as_view(), name='trainings_list'),
    path('trainings/<int:pk>/details/',TrainingsDetailV.as_view(), name='trainings_details'),
    #CUSTOM EVENTS section
    path('customs/', CustomEventsListV.as_view(), name='custom_events_list'),
    path('customs/<int:pk>/details/',CustomEventsDetailV.as_view(), name='custom_events_details'),
]