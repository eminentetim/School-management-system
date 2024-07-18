from django import forms
from .models import CustomUser, Profile, Role, Permission, UserRole, UserActivityLog

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'two_factor_enabled', 'sso_id']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'two_factor_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sso_id': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'date_of_birth', 'address']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name']
        widgets = {
            'role_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['permission_name']
        widgets = {
            'permission_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['user', 'role']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

class UserActivityLogForm(forms.ModelForm):
    class Meta:
        model = UserActivityLog
        fields = ['user', 'activity']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'activity': forms.Textarea(attrs={'class': 'form-control'}),
        }

