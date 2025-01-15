from django.urls import path, include
from teams.views import TeamListV, TeamDetailV, PlayersAffiliationsV, PlayersAffiliationsCreateV, EndPlayerAffiliation

urlpatterns = [
    path('' , TeamListV.as_view(), name='teams_list'),
    path('squad/', TeamDetailV.as_view(), name='team_details'),

    path('affiliations/', PlayersAffiliationsCreateV.as_view(), name='create_players_affiliations'),
    path('affiliations/<int:id>/', PlayersAffiliationsV.as_view(), name='player_affiliations'),
    path('affiliations/end/<int:id>/', EndPlayerAffiliation.as_view(), name='end_player_affiliations'),
]