from rest_framework import generics, status
from rest_framework.response import Response
from teams.models import Teams, PlayersAffilations, TeamSquad
from teams.serizalizers import TeamSerializer, PlayersAffilationsSerializer, TeamDetailsSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TeamListV(generics.ListCreateAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


class TeamDetailV(generics.ListAPIView):
    queryset = TeamSquad.objects.all()
    serializer_class = TeamDetailsSerializer
    lookup_field = 'team_id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['team_id']

class PlayersAffiliationsCreateV(generics.CreateAPIView):
    queryset = PlayersAffilations.objects.all()
    serializer_class = PlayersAffilationsSerializer


class EndPlayerAffiliation(generics.UpdateAPIView):
    queryset = PlayersAffilations.objects.all()
    serializer_class = PlayersAffilationsSerializer
    lookup_field = 'id'

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        end_date = request.data.get('end_date')

        if end_date is not None:
            instance.end_date = end_date
            instance.save()
            return Response(self.get_serializer(instance).data)

        return Response({'detail': 'end_date not provided'}, status=status.HTTP_400_BAD_REQUEST)
    

class PlayersAffiliationsV(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayersAffilations.objects.all()
    serializer_class = PlayersAffilationsSerializer
    lookup_field = 'id'


