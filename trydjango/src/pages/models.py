from django.db import models
import datetime

# Create your models here.
class Word(models.Model):
    word        = models.CharField(max_length=100)
    definition  = models.TextField(null=True, blank=True, default="Definition")
    examples    = models.TextField(null=True, blank=True, default="Examples")
    updater     = models.CharField(max_length=100, default="anonym")
    city        = models.CharField(max_length=100, default="Moscow")
    date        = models.CharField(max_length=100, default=datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"))