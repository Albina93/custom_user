from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    displayname = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    url = models.URLField(null=True)
    REQUIRED_FIELDS = ['age']




    def __str__(self):
        return self.username