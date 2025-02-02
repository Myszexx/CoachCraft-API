from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN

from apps.core.models import AuthUser
from apps.core.serializers import RegistrationSerializer
from apps.core.utils import get_tokens_for_user
from rest_framework.response import Response

class RegistrationV(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = AuthUser.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        data = {}
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print("VALID")
            if serializer.validated_data['password2'] != serializer.validated_data['password']:
                data['response'] = ['Passwords do not match']
                return Response(data, status=HTTP_403_FORBIDDEN)
            print("PERFORM")
            account = serializer.save()
            token = get_tokens_for_user(account)
            data['response'] = ['Account created successfully']
            data['email'] = [account.email]
            data['username'] = [account.username]
            data['user_id'] = [account.id]
            data['token'] = token
        else:
            return Response(serializer.errors)
        return Response(data, status=HTTP_201_CREATED)