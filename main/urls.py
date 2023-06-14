from django.urls import path, include
from .views import (HomePage, PasswordChange, DeviceManaging, DeviceEdit, DeviceDelete, DeviceCreate,
                    GroupManaging, GroupEdit, GroupCreate,
                    Manage, AdminDeviceEdit, AdminDeviceDelete, AdminDeviceCreate,
                    UserManaging, UserCreate, UserEdit, UserDelete,
                    BatchCreateUser)

urlpatterns = [
    # 首頁路徑
    path('', HomePage.as_view(), name='homepage'),

    # 裝置相關路徑
    path('devices/', DeviceManaging.as_view(), name='device_managing'),
    path('devices/edit/<int:deviceid>/', DeviceEdit.as_view(), name='device_edit'),
    path('devices/delete/<int:deviceid>/', DeviceDelete.as_view(), name='device_delete'),
    path('devices/create/', DeviceCreate.as_view(), name='device_create'),

    # 帳號相關路徑
    path('auth/password/', PasswordChange.as_view(), name='password'),
    path('auth/', include('django.contrib.auth.urls')),
    # path('auth/registation', register, name='register'),

    #管理員 裝置 相關路徑
    path('manage/', Manage.as_view(), name='manage'),
    path('manage/edit/<int:deviceid>/', AdminDeviceEdit.as_view(), name='admin_device_edit'),
    path('manage/delete/<int:deviceid>/', AdminDeviceDelete.as_view(), name='admin_device_delete'),
    path('manage/create/', AdminDeviceCreate.as_view(), name='admin_device_create'),

    #管理員 群組 相關路徑
    path('group/', GroupManaging.as_view(), name='group_managing'),
    path('group/edit/<int:groupid>/', GroupEdit.as_view(), name='group_edit'),
    # path('group/delete/<int:groupid>/', GroupDelete.as_view(), name='group_delete'),
    path('group/create/', GroupCreate.as_view(), name='group_create'),

    #管理員 人員 相關路徑
    path('user/', UserManaging.as_view(), name='user_managing'),
    path('user/create/', UserCreate.as_view(), name='user_create'),
    path('user/edit/<int:userid>/', UserEdit.as_view(), name='user_edit'),
    path('user/delete/<int:userid>/', UserDelete.as_view(), name='user_delete'),

    path('user/create/batch/', BatchCreateUser.as_view(), name='user_batch_create'),
]
