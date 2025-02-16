from django.contrib.auth.models import User
from django.db import models


class UserData(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    phone = models.CharField(max_length=1024, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.CharField(max_length=1024, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_data'