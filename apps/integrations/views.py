from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

from API.integrations.PFScrapper.grcp_client import GRPCClient as grcp
from apps.integrations.serializers import LinkedListSerializer


# Create your views here.

class ZPNsListV(generics.RetrieveAPIView):
    serializer_class = LinkedListSerializer

    def get(self, request):
        data = grcp().get_data('/ligireg.html')
        if not LinkedListSerializer(data).is_valid():
            return Response(status=HTTP_204_NO_CONTENT)

        return Response(data, status=HTTP_200_OK)