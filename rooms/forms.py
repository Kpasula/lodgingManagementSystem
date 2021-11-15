from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import DateTimeInput

from .models import Rooms, AllocatedRooms


class CheckInForm(forms.ModelForm):
    class Meta:
        model = AllocatedRooms
        fields = ('room_assigned', 'client_assigned', 'allocated_by', 'check_in_date', 'check_out_date', 'payment_id')
        widgets = {
            'check_in_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'check_out_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(CheckInForm, self).__init__(*args, **kwargs)
        self.fields['room_assigned'].queryset = Rooms.objects.filter(assigned=False)


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = AllocatedRooms
        fields = ('checked_out',)
