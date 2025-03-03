
from django.urls import path, include

from apps.integrations.views import ZPNsListV

urlpatterns = [
#90mins scrapper
    path('90mins/ZPNs/', ZPNsListV.as_view(), name='zpn_list'),
]