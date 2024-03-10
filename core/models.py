from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=4)
    contact = models.IntegerField()


    def __str__(self) -> str:
        return f"{self.name}"
