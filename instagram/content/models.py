from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class PhotoPost(models.Model):
    author = models.ForeignKey(User)
    image = models.ImageField()
    description = models.TextField()

