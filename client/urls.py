from django.urls import path

from .views import ClientNewView, ClientUpdateView, ClientCreateView

urlpatterns = [
    path('<int:pk>/client/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('client/create/',
         ClientCreateView.as_view(), name='client_create'),
    path('client/', ClientNewView.as_view(), name='client_new'),
    path('', ClientNewView.as_view(), name='client_list'),
]
