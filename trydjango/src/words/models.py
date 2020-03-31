from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from likes.models import Like
from likes.models import Dislike
import datetime

# Create your models here.
class Word(models.Model):
    word        = models.CharField(max_length=100)
    definition  = models.TextField(null=True, blank=True, default="Definition")
    examples    = models.TextField(null=True, blank=True, default="Examples")
    updater     = models.CharField(max_length=100, default="anonym")
    city        = models.CharField(max_length=100, default="Moscow")
    date        = models.CharField(max_length=100, default=datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"))
    likes = GenericRelation(Like)
    dislikes = GenericRelation(Dislike)
    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_dislikes(self):
        return self.dislikes.count()
