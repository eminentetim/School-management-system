# user_management/admin.py
from django.contrib import admin
from django.contrib import registrar
from .models import Student, Class, Enrollment, Attendance, Grade
from .models import User, Role, Permission, UserRole, UserActivityLog, Profile

admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(UserActivityLog, UserActivityLogAdmin)
admin.site.register(Profile, ProfileAdmin)

"""student information """

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(Grade)
