from django.db import models
from apps.events.utils import get_current_season
# Create your models here.

class LinkedList(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    class Meta:
        abstract = True

class ZPNs(LinkedList):
    pass
    class Meta:
        db_table = 'ninety_mins"."zpns'
        managed = True

class Leagues(LinkedList):
    season = models.CharField(max_length=255, default=get_current_season())
    zpn = models.ForeignKey(ZPNs, on_delete=models.CASCADE)
    class Meta:
        db_table = 'ninety_mins"."leagues'
        managed = True

class Table(LinkedList):
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    matches = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_conceded = models.IntegerField()
    points = models.IntegerField()
    position = models.IntegerField()
    class Meta:
        db_table = 'ninety_mins"."table'
        managed = True

class Fixtures(models.Model):
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    class Meta:
        db_table = 'ninety_mins"."fixtures'
        managed = True

class MatchEvents(models.Model):
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    time = models.IntegerField()
    player = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)
    class Meta:
        db_table = 'ninety_mins"."match_events'
        managed = True