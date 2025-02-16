
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.core.views import RegistrationV, LoginV, UserDataV

urlpatterns = [
    path('users_data/<int:pk>', UserDataV.as_view(), name='users_data'),
    path('registration/', RegistrationV.as_view(), name='registration'),
    path('login/', LoginV.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
