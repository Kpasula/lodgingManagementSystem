from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView, CreateView

from client.models import Client


class ClientNewView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client/client_new.html'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy('client_list')
    fields = ('name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'staff')
    template_name = 'client/client_edit.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    success_url = reverse_lazy('client_list')
    fields = ('name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'staff')
    template_name = 'client/client_create.html'
    login_url = 'login'


    def form_valid(self, form):
        return super().form_valid(form)
