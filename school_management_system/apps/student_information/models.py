from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_info = models.JSONField()
    academic_info = models.JSONField()
    guardian_info = models.JSONField()
    disciplinary_info = models.JSONField()

    def __str__(self):
        return self.user.username

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    withdrawal_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.student.user.username} - {self.class_id.class_name}'

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    timetable = models.JSONField()
    room_allocation = models.JSONField()

    def __str__(self):
        return self.class_name

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.student.user.username} - {self.class_id.class_name} on {self.attendance_date}'

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.student.user.username} - {self.class_id.class_name}: {self.grade}'

