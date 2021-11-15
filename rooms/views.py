from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import CheckInForm, CheckOutForm
from .models import Rooms, AllocatedRooms


class RoomListView(LoginRequiredMixin, ListView):
    model = AllocatedRooms
    template_name = 'rooms/room_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allocated_rooms = AllocatedRooms.objects.all()
        context['rooms'] = allocated_rooms.filter(checked_out=False)
        context['available_rooms'] = Rooms.objects.filter(assigned=False).count()
        return context


class RoomCheckinView(LoginRequiredMixin, CreateView):
    form_class = CheckInForm
    template_name = 'rooms/checkin.html'


class CheckOutUpdateView(LoginRequiredMixin, UpdateView):
    model = AllocatedRooms
    success_url = reverse_lazy('room_list')
    form_class = CheckOutForm
    template_name = 'rooms/check_out.html'


