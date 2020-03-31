from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Dislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='dislikes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

# also known as services.py

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
User = get_user_model()


def add_like(obj, user):
    """ Ставит лайк определению """
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return like


def remove_like(obj, user):
    """ Удаляет лайк с определения """
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def add_dislike(obj, user):
    """ Ставит дислайк определению """
    obj_type = ContentType.objects.get_for_model(obj)
    dislike, is_created = Dislike.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return dislike


def remove_dislike(obj, user):
    """ Удаляет дислайк с определения """
    obj_type = ContentType.objects.get_for_model(obj)
    Dislike.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()

