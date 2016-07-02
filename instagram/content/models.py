from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class PhotoPost(models.Model):
    image = models.ImageField()
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)


class Comment(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()


class Like(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(PhotoPost)
