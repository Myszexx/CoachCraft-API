# from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from apps.players.models import Players, Ratings
from apps.players.serializers import PlayersSerializer, RatingsSerializer
from API.permissions import RatingUserOrAdmin


# Create your views here.


class PlayerMVS(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer

class RatingsList(generics.ListAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer

    # def perform_create(self, serializer):
    #     data = self.request.
    #     serializer.save(rating_user=self.request.user)
class RatingsCreate(generics.CreateAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    permission_classes = [RatingUserOrAdmin]

    def perform_create(self, serializer):
        match_id = self.kwargs.get('match_id')
        training_id = self.kwargs.get('training_id')
        player_id = self.kwargs.get('player_id')

        rating_user = self.request.user
        if match_id:
            rating_query = Ratings.objects.filter(match_id=match_id, player_id=player_id)
        else:
            rating_query = Ratings.objects.filter(training_id=training_id, player_id=player_id)

        if rating_query.exists():
            raise ValidationError("You have already rated this player")
        serializer.save(rating_user=self.request.user)

class PlayerDetail(generics.RetrieveUpdateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    lookup_field = 'pk'