from django.db import models
# Create your models here.

class Teams(models.Model):
    team_name = models.CharField(max_length=64, blank=True, null=True)
    logo = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'


#VW
class TeamSquad(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey("players.Players", models.DO_NOTHING, related_name='player_set')
    team = models.ForeignKey(Teams, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'actual_players_affiliations'
    #Making model read-only
    def save(self, *args, **kwargs):
        return
    def delete(self, *args, **kwargs):
        return



class PlayersAffilations(models.Model):
    player = models.ForeignKey("players.Players", models.DO_NOTHING)
    team = models.ForeignKey('Teams', models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players_affilations'





class UserTeams(models.Model):
    user = models.ForeignKey("core.AuthUser", models.DO_NOTHING)
    team = models.ForeignKey(Teams, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_teams'