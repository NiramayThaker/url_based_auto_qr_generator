from django.db import models
import uuid 


class UserInfo(models.Model):
    user_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=4)
    contact = models.IntegerField()


    def __str__(self) -> str:
        return f"{self.name}"
