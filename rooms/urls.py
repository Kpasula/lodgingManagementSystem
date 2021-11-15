from django.urls import path

from rooms import views
from rooms.views import CheckOutUpdateView

urlpatterns = [
    path('rooms/checkin', views.RoomCheckinView.as_view(), name='checkin'),
    path('', views.RoomListView.as_view(), name='room_list'),
    path('<int:pk>/rooms/check_out/',
         CheckOutUpdateView.as_view(), name='check_out'),

]
