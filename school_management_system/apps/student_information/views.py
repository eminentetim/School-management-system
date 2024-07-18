from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student, Enrollment, Class, Attendance, Grade
from .forms import StudentForm, EnrollmentForm, ClassForm, AttendanceForm, GradeForm

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_information/student_list.html'
    context_object_name = 'students'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_information/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_information/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_information/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')

class EnrollmentListView(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = 'student_information/enrollment_list.html'
    context_object_name = 'enrollments'

class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'student_information/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

class EnrollmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'student_information/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

class EnrollmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Enrollment
    template_name = 'student_information/enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollment-list')

class ClassListView(LoginRequiredMixin, ListView):
    model = Class
    template_name = 'student_information/class_list.html'
    context_object_name = 'classes'

class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'student_information/class_form.html'
    success_url = reverse_lazy('class-list')

class ClassUpdateView(LoginRequiredMixin, UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'student_information/class_form.html'
    success_url = reverse_lazy('class-list')

class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Class
    template_name = 'student_information/class_confirm_delete.html'
    success_url = reverse_lazy('class-list')

class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'student_information/attendance_list.html'
    context_object_name = 'attendances'

class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'student_information/attendance_form.html'
    success_url = reverse_lazy('attendance-list')

class AttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'student_information/attendance_form.html'
    success_url = reverse_lazy('attendance-list')

class AttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'student_information/attendance_confirm_delete.html'
    success_url = reverse_lazy('attendance-list')

class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'student_information/grade_list.html'
    context_object_name = 'grades'

class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'student_information/grade_form.html'
    success_url = reverse_lazy('grade-list')

class GradeUpdateView(LoginRequiredMixin, UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'student_information/grade_form.html'
    success_url = reverse_lazy('grade-list')

class GradeDeleteView(LoginRequiredMixin, DeleteView):
    model = Grade
    template_name = 'student_information/grade_confirm_delete.html'
    success_url = reverse_lazy('grade-list')

