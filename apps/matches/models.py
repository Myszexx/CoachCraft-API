from django.db import models

# Create your models here.

class Matches(models.Model):
    home_team = models.ForeignKey('teams.Teams', models.DO_NOTHING, blank=True, null=True)
    home_team_name = models.CharField(max_length=1024, blank=True, null=True)
    away_team = models.ForeignKey('teams.Teams', models.DO_NOTHING, related_name='matches_away_team_set', blank=True, null=True)
    away_team_name = models.CharField(max_length=1024, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'matches'



class MatchSquad(models.Model):
    match = models.ForeignKey(Matches, models.DO_NOTHING)
    is_home_team = models.BooleanField(blank=True, null=True)
    player = models.ForeignKey('players.Players', models.DO_NOTHING)
    numer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match_squad'

class MatchEvents(models.Model):
    match = models.ForeignKey('Matches', models.DO_NOTHING)
    minute = models.IntegerField()
    player = models.ForeignKey('players.Players', models.DO_NOTHING, blank=True, null=True)
    player2 = models.ForeignKey('players.Players', models.DO_NOTHING, related_name='matchevents_player2_set', blank=True, null=True)
    half = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match_events'

class MatchEventTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024)
    icon = models.CharField(max_length=1024, blank=True, null=True)
    type = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'match_event_types'