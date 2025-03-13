
from django.urls import path, include

from apps.integrations.views import ZPNsListV, LeaguesListV, TableListV, FixturesListV

# from apps.integrations.views import ZPNsListV

urlpatterns = [
#90mins scrapper
    # path('90mins/', NinetyMinsListV.as_view(), name='NinetyMinsData'),
    path('90mins/zpn/',ZPNsListV.as_view(), name='ZPNsData'),
    path('90mins/leagues/',LeaguesListV.as_view(), name='LeaguesData'),
    path('90mins/table/',TableListV.as_view(), name='TableData'),
    path('90mins/fixtures/',FixturesListV.as_view(), name='FixturesData'),

]