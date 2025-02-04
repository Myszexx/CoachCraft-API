from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN, HTTP_200_OK

from apps.core.models import AuthUser
from apps.core.serializers import RegistrationSerializer, LoginSerializer
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

class LoginV(generics.RetrieveAPIView):
    serializer_class = LoginSerializer
    queryset = AuthUser.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.filter(username=self.request.GET.get('username'))

    def post(self, request, *args, **kwargs):
        data = {}
        if request.data['username'] == '' or request.data['password'] == '':
            data['response'] = ['Please provide all required fields']
            return Response(data, status=HTTP_403_FORBIDDEN)
        try:
            print(request.data)
            account = AuthUser.objects.get(username=request.data['username'])
            token = get_tokens_for_user(account)
            data['response'] = ['Login successful']
            data['email'] = [account.email]
            data['username'] = [account.username]
            data['user_id'] = [account.id]
            data['token'] = token
        except AuthUser.DoesNotExist:
            data['error'] = "User does not exist"
            return Response(data, status=HTTP_403_FORBIDDEN)
        return Response(data, status=HTTP_200_OK)