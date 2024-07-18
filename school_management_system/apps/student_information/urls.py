from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    EnrollmentListView, EnrollmentCreateView, EnrollmentUpdateView, EnrollmentDeleteView,
    ClassListView, ClassCreateView, ClassUpdateView, ClassDeleteView,
    AttendanceListView, AttendanceCreateView, AttendanceUpdateView, AttendanceDeleteView,
    GradeListView, GradeCreateView, GradeUpdateView, GradeDeleteView
)

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/create/', StudentCreateView.as_view(), name='student-create'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/create/', EnrollmentCreateView.as_view(), name='enrollment-create'),
    path('enrollments/update/<int:pk>/', EnrollmentUpdateView.as_view(), name='enrollment-update'),
    path('enrollments/delete/<int:pk>/', EnrollmentDeleteView.as_view(), name='enrollment-delete'),
    
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('classes/create/', ClassCreateView.as_view(), name='class-create'),
    path('classes/update/<int:pk>/', ClassUpdateView.as_view(), name='class-update'),
    path('classes/delete/<int:pk>/', ClassDeleteView.as_view(), name='class-delete'),
    
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('attendance/create/', AttendanceCreateView.as_view(), name='attendance-create'),
    path('attendance/update/<int:pk>/', AttendanceUpdateView.as_view(), name='attendance-update'),
    path('attendance/delete/<int:pk>/', AttendanceDeleteView.as_view(), name='attendance-delete'),
    
    path('grades/', GradeListView.as_view(), name='grade-list'),
    path('grades/create/', GradeCreateView.as_view(), name='grade-create'),
    path('grades/update/<int:pk>/', GradeUpdateView.as_view(), name='grade-update'),
    path('grades/delete/<int:pk>/', GradeDeleteView.as_view(), name='grade-delete'),
]

