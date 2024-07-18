from django.urls import path
from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    ProfileListView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView,
    RoleListView, RoleCreateView, RoleUpdateView, RoleDeleteView,
    PermissionListView, PermissionCreateView, PermissionUpdateView, PermissionDeleteView,
    UserRoleListView, UserRoleCreateView, UserRoleUpdateView, UserRoleDeleteView,
    UserActivityLogListView, UserActivityLogCreateView, UserActivityLogUpdateView, UserActivityLogDeleteView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),

    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profiles/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profiles/delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile-delete'),

    path('roles/', RoleListView.as_view(), name='role-list'),
    path('roles/create/', RoleCreateView.as_view(), name='role-create'),
    path('roles/update/<int:pk>/', RoleUpdateView.as_view(), name='role-update'),
    path('roles/delete/<int:pk>/', RoleDeleteView.as_view(), name='role-delete'),

    path('permissions/', PermissionListView.as_view(), name='permission-list'),
    path('permissions/create/', PermissionCreateView.as_view(), name='permission-create'),
    path('permissions/update/<int:pk>/', PermissionUpdateView.as_view(), name='permission-update'),
    path('permissions/delete/<int:pk>/', PermissionDeleteView.as_view(), name='permission-delete'),

    path('userroles/', UserRoleListView.as_view(), name='userrole-list'),
    path('userroles/create/', UserRoleCreateView.as_view(), name='userrole-create'),
    path('userroles/update/<int:pk>/', UserRoleUpdateView.as_view(), name='userrole-update'),
    path('userroles/delete/<int:pk>/', UserRoleDeleteView.as_view(), name='userrole-delete'),

    path('useractivitylogs/', UserActivityLogListView.as_view(), name='useractivitylog-list'),
    path('useractivitylogs/create/', UserActivityLogCreateView.as_view(), name='useractivitylog-create'),
    path('useractivitylogs/update/<int:pk>/', UserActivityLogUpdateView.as_view(), name='useractivitylog-update'),
    path('useractivitylogs/delete/<int:pk>/', UserActivityLogDeleteView.as_view(), name='useractivitylog-delete'),
]

