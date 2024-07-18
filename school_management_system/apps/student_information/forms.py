from django import forms
from .models import Student, Enrollment, Class, Attendance, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'personal_info', 'academic_info', 'guardian_info', 'disciplinary_info']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'personal_info': forms.Textarea(attrs={'class': 'form-control'}),
            'academic_info': forms.Textarea(attrs={'class': 'form-control'}),
            'guardian_info': forms.Textarea(attrs={'class': 'form-control'}),
            'disciplinary_info': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'class_id', 'enrollment_date', 'withdrawal_date']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'withdrawal_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'timetable', 'room_allocation']
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'timetable': forms.Textarea(attrs={'class': 'form-control'}),
            'room_allocation': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'class_id', 'attendance_date', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'attendance_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'class_id', 'grade']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }

