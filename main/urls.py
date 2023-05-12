from django.contrib import admin
from django.urls import path
from .views import DeviceManaging, DeviceEdit, DeviceDelete, DeviceCreate

urlpatterns = [
    path('devices/', DeviceManaging.as_view(), name='device_managing'),
    path('devices/edit/<int:deviceid>/', DeviceEdit.as_view(), name='device_edit'),
    path('devices/delete/<int:deviceid>/', DeviceDelete.as_view(), name='device_delete'),
    path('devices/create/', DeviceCreate.as_view(), name='device_create'),
]
