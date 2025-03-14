from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Players(models.Model):
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    country = models.CharField(max_length=5, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players'


    # def __str__(self):
    #     return self.first_name + " " + self.last_name

# class PlayerAffilation(models.Model):
#     id = models.AutoField(primary_key=True)
#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     team = models.ForeignKey("Team", on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)

    
class Ratings(models.Model):
    rating_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    training = models.ForeignKey('events.TrainingSquad', models.DO_NOTHING, blank=True, null=True)
    match = models.ForeignKey('events.Matches', models.DO_NOTHING, blank=True, null=True)
    player = models.ForeignKey(Players, models.DO_NOTHING)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'




