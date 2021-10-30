from django.urls import path
from roomapp import views

urlpatterns = [
    path('rooms/', views.room_list),
    path('rooms/<int:room_id>/', views.room_detail),
    path('rooms/<int:room_id>/join', views.join_room),
]
