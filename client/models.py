from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    address = models.CharField(max_length=50, blank=True, null=True, default=' ')
    city = models.CharField(max_length=50, default='Omaha')
    state = models.CharField(max_length=15, default='NE')
    zipcode = models.CharField(max_length=6, default='00000')
    email = models.EmailField(max_length=100, default='@gmail.com')
    cell_phone = models.CharField(max_length=13, default='(402)000-0000')

    staff = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, null=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])
