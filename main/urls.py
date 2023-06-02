from django.urls import path, include
from .views import HomePage, PasswordChange, DeviceManaging, DeviceEdit, DeviceDelete, DeviceCreate, GroupManaging, GroupEdit, GroupDelete, GroupCreate, Manage

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

    #管理員 群組 相關路徑
    path('group/', GroupManaging.as_view(), name='group_managing'),
    path('group/edit/<int:groupid>', GroupEdit.as_view(), name='group_edit'),
    path('group/delete/<int:groupid>', GroupDelete.as_view(), name='group_delete'),
    path('group/create/', GroupCreate.as_view(), name='group_create'),
    path('manage/', Manage.as_view(), name='manage'),
    
]
