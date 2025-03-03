from django.db import models

# Create your models here.

class LinkedList(models.Model):
    url = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    
    class Meta:
        abstract = True