from django.urls import path, include
from .views import HomePage, PasswordChange, DeviceManaging, DeviceEdit, DeviceDelete, DeviceCreate

urlpatterns = [
    # 首頁路徑
    path('', HomePage.as_view(), name='homepage'),

    # 裝置相關路徑
    path('devices/', DeviceManaging.as_view(), name='device_managing'),
    path('devices/edit/<int:deviceid>/', DeviceEdit.as_view(), name='device_edit'),
    path('devices/delete/<int:deviceid>/', DeviceDelete.as_view(), name='device_delete'),
    path('devices/create/', DeviceCreate.as_view(), name='device_create'),

    # 帳號相關路徑
    path('auth/', include('django.contrib.auth.urls')),
    # path('auth/registation', register, name='register'),
    path('auth/password/', PasswordChange.as_view(), name='password'),
]
