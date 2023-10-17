from django.db import models
from django.contrib.auth.models import AbstractUser


class Thing(AbstractUser):
    name = models.CharField()
    description = models.TextField()
    quatity = models.IntegerField()
