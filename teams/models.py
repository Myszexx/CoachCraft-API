from django.db import models
# Create your models here.

class Teams(models.Model):
    team_name = models.CharField(max_length=64, blank=True, null=True)
    logo = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'

class PlayersAffilations(models.Model):
    player = models.ForeignKey("players.player", models.DO_NOTHING)
    team = models.ForeignKey(Teams, models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players_affilations'

class Trainings(models.Model):
    team = models.ForeignKey(Teams, models.DO_NOTHING)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainings'