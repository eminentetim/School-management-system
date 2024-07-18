from django.contrib import admin
from .models import Student, Class, Enrollment, Attendance, Grade

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(Grade)

