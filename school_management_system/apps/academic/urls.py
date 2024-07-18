from django.urls import path
from .views import (
    CurriculumListView, CurriculumCreateView, CurriculumUpdateView, CurriculumDeleteView,
    LessonListView, LessonCreateView, LessonUpdateView, LessonDeleteView,
    ExamListView, ExamCreateView, ExamUpdateView, ExamDeleteView,
    AssessmentListView, AssessmentCreateView, AssessmentUpdateView, AssessmentDeleteView,
    ReportCardListView, ReportCardCreateView, ReportCardUpdateView, ReportCardDeleteView
)

urlpatterns = [
    path('curriculums/', CurriculumListView.as_view(), name='curriculum-list'),
    path('curriculums/create/', CurriculumCreateView.as_view(), name='curriculum-create'),
    path('curriculums/update/<int:pk>/', CurriculumUpdateView.as_view(), name='curriculum-update'),
    path('curriculums/delete/<int:pk>/', CurriculumDeleteView.as_view(), name='curriculum-delete'),

    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('lessons/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lessons/delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson-delete'),

    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('exams/create/', ExamCreateView.as_view(), name='exam-create'),
    path('exams/update/<int:pk>/', ExamUpdateView.as_view(), name='exam-update'),
    path('exams/delete/<int:pk>/', ExamDeleteView.as_view(), name='exam-delete'),

    path('assessments/', AssessmentListView.as_view(), name='assessment-list'),
    path('assessments/create/', AssessmentCreateView.as_view(), name='assessment-create'),
    path('assessments/update/<int:pk>/', AssessmentUpdateView.as_view(), name='assessment-update'),
    path('assessments/delete/<int:pk>/', AssessmentDeleteView.as_view(), name='assessment-delete'),

    path('reportcards/', ReportCardListView.as_view(), name='reportcard-list'),
    path('reportcards/create/', ReportCardCreateView.as_view(), name='reportcard-create'),
    path('reportcards/update/<int:pk>/', ReportCardUpdateView.as_view(), name='reportcard-update'),
    path('reportcards/delete/<int:pk>/', ReportCardDeleteView.as_view(), name='reportcard-delete'),
]

