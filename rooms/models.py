from django.db import models

# Create your models here.
from django.urls import reverse

from staff.models import CustomUser
from client.models import Client


class Rooms(models.Model):
    RoomType = models.TextChoices('RoomType', 'NON-SMOKING_KING NON-SMOKING_QUEEN NON-SMOKING_DOUBLE_BED SMOKING_KING SMOKING_QUEEN SMOKING_DOUBLE_BED')
    number = models.IntegerField()
    assigned = models.BooleanField(default=False)
    room_type = models.CharField(blank=True, choices=RoomType.choices, max_length=255)

    def __str__(self):
        return '{}, {}'.format(self.number, self.room_type)


class AllocatedRooms(models.Model):
    room_assigned = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='allocated_room')
    client_assigned = models.ForeignKey(Client, on_delete=models.PROTECT)
    allocated_by = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    checked_out = models.BooleanField(default=False)
    payment_id = models.CharField(blank=False, null=False, max_length=200)

    def get_absolute_url(self):
        return reverse('room_list')

    def save(self, *args, **kwargs):
        self.room_assigned.assigned = not self.checked_out
        self.room_assigned.save()
        return super().save(*args, **kwargs)
