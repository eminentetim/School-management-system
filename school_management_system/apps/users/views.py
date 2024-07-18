from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CustomUser, Profile, Role, Permission, UserRole, UserActivityLog
from .forms import UserForm, ProfileForm, RoleForm, PermissionForm, UserRoleForm, UserActivityLogForm

class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user_management/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'user_management/user_form.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'user_management/user_form.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'user_management/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        return self.request.user.is_superuser

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'user_management/profile_list.html'
    context_object_name = 'profiles'

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user_management/profile_form.html'
    success_url = reverse_lazy('profile-list')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'user_management/profile_form.html'
    success_url = reverse_lazy('profile-list')

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'user_management/profile_confirm_delete.html'
    success_url = reverse_lazy('profile-list')


class RoleListView(LoginRequiredMixin, ListView):
    model = Role
    template_name = 'user_management/role_list.html'
    context_object_name = 'roles'

class RoleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'user_management/role_form.html'
    success_url = reverse_lazy('role-list')

    def test_func(self):
        return self.request.user.is_superuser

class RoleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'user_management/role_form.html'
    success_url = reverse_lazy('role-list')

    def test_func(self):
        return self.request.user.is_superuser

class RoleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Role
    template_name = 'user_management/role_confirm_delete.html'
    success_url = reverse_lazy('role-list')

    def test_func(self):
        return self.request.user.is_superuser

class PermissionListView(LoginRequiredMixin, ListView):
    model = Permission
    template_name = 'user_management/permission_list.html'
    context_object_name = 'permissions'

class PermissionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Permission
    form_class = PermissionForm
    template_name = 'user_management/permission_form.html'
    success_url = reverse_lazy('permission-list')

    def test_func(self):
        return self.request.user.is_superuser

class PermissionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Permission
    form_class = PermissionForm
    template_name = 'user_management/permission_form.html'
    success_url = reverse_lazy('permission-list')

    def test_func(self):
        return self.request.user.is_superuser

class PermissionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Permission
    template_name = 'user_management/permission_confirm_delete.html'
    success_url = reverse_lazy('permission-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserRoleListView(LoginRequiredMixin, ListView):
    model = UserRole
    template_name = 'user_management/userrole_list.html'
    context_object_name = 'userroles'

class UserRoleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = UserRole
    form_class = UserRoleForm
    template_name = 'user_management/userrole_form.html'
    success_url = reverse_lazy('userrole-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserRoleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserRole
    form_class = UserRoleForm
    template_name = 'user_management/userrole_form.html'
    success_url = reverse_lazy('userrole-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserRoleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserRole
    template_name = 'user_management/userrole_confirm_delete.html'
    success_url = reverse_lazy('userrole-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserActivityLogListView(LoginRequiredMixin, ListView):
    model = UserActivityLog
    template_name = 'user_management/useractivitylog_list.html'
    context_object_name = 'useractivitylogs'

class UserActivityLogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = UserActivityLog
    form_class = UserActivityLogForm
    template_name = 'user_management/useractivitylog_form.html'
    success_url = reverse_lazy('useractivitylog-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserActivityLogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserActivityLog
    form_class = UserActivityLogForm
    template_name = 'user_management/useractivitylog_form.html'
    success_url = reverse_lazy('useractivitylog-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserActivityLogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserActivityLog
    template_name = 'user_management/useractivitylog_confirm_delete.html'
    success_url = reverse_lazy('useractivitylog-list')

    def test_func(self):
        return self.request.user.is_superuser

