from django.contrib import admin
from .models import CustomUser, Profile, Role, Permission, UserRole, UserActivityLog

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserRole)
admin.site.register(UserActivityLog)
