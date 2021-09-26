from django.db import models

# Create your models here.

from staff.models import CustomUser
from client.models import Client


class Rooms(models.Model):
    RoomType = models.TextChoices('RoomType', 'NON-SMOKING_KING NON-SMOKING_QUEEN NON-SMOKING_DOUBLE_BED'
                                              'SMOKING_KING SMOKING_QUEEN SMOKING_DOUBLE_BED')
    number = models.IntegerField()
    room_type = models.CharField(blank=True, choices=RoomType.choices, max_length=255)


class AllocatedRooms(models.Model):
    room_assigned = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    client_assigned = models.ForeignKey(Client, on_delete=models.PROTECT)
    allocated_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
