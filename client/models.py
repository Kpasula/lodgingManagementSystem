from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Client(models.Model):

    name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    address = models.CharField(max_length=50, blank=True, null=True,default=' ')
    city = models.CharField(max_length=50, default='Omaha')
    state = models.CharField(max_length=15, default='NE')
    zipcode = models.CharField(max_length=6, default='00000')
    email = models.EmailField(max_length=100, default='@gmail.com')
    cell_phone = models.CharField(max_length=13,default='(402)000-0000')
    card_number = models.CharField(max_length=16,blank=True, null=True, default='0000000000000000')
    card_expiration_month = models.CharField(max_length=2, blank=True, null=True, default='00')
    card_expiration_year = models.CharField(max_length=2, blank=True, null=True, default='00')
    card_cvv = models.CharField(max_length=3, blank=True, null=True, default='000')
    room_type = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])
