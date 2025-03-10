
from django.urls import path, include

from apps.integrations.views import NinetyMinsListV

# from apps.integrations.views import ZPNsListV

urlpatterns = [
#90mins scrapper
    path('90mins/ZPNs/', NinetyMinsListV.as_view(), name='NinetyMinsData'),
]