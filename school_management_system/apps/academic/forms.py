from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Curriculum, Lesson, Exam, Assessment, ReportCard
from .forms import CurriculumForm, LessonForm, ExamForm, AssessmentForm, ReportCardForm

class CurriculumListView(LoginRequiredMixin, ListView):
    model = Curriculum
    template_name = 'academic_management/curriculum_list.html'
    context_object_name = 'curriculums'

class CurriculumCreateView(LoginRequiredMixin, CreateView):
    model = Curriculum
    form_class = CurriculumForm
    template_name = 'academic_management/curriculum_form.html'
    success_url = reverse_lazy('curriculum-list')

class CurriculumUpdateView(LoginRequiredMixin, UpdateView):
    model = Curriculum
    form_class = CurriculumForm
    template_name = 'academic_management/curriculum_form.html'
    success_url = reverse_lazy('curriculum-list')

class CurriculumDeleteView(LoginRequiredMixin, DeleteView):
    model = Curriculum
    template_name = 'academic_management/curriculum_confirm_delete.html'
    success_url = reverse_lazy('curriculum-list')

class LessonListView(LoginRequiredMixin, ListView):
    model = Lesson
    template_name = 'academic_management/lesson_list.html'
    context_object_name = 'lessons'

class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'academic_management/lesson_form.html'
    success_url = reverse_lazy('lesson-list')

class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'academic_management/lesson_form.html'
    success_url = reverse_lazy('lesson-list')

class LessonDeleteView(LoginRequiredMixin, DeleteView):
    model = Lesson
    template_name = 'academic_management/lesson_confirm_delete.html'
    success_url = reverse_lazy('lesson-list')

class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'academic_management/exam_list.html'
    context_object_name = 'exams'

class ExamCreateView(LoginRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'academic_management/exam_form.html'
    success_url = reverse_lazy('exam-list')

class ExamUpdateView(LoginRequiredMixin, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'academic_management/exam_form.html'
    success_url = reverse_lazy('exam-list')

class ExamDeleteView(LoginRequiredMixin, DeleteView):
    model = Exam
    template_name = 'academic_management/exam_confirm_delete.html'
    success_url = reverse_lazy('exam-list')

class AssessmentListView(LoginRequiredMixin, ListView):
    model = Assessment
    template_name = 'academic_management/assessment_list.html'
    context_object_name = 'assessments'

class AssessmentCreateView(LoginRequiredMixin, CreateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = 'academic_management/assessment_form.html'
    success_url = reverse_lazy('assessment-list')

class AssessmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = 'academic_management/assessment_form.html'
    success_url = reverse_lazy('assessment-list')

class AssessmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Assessment
    template_name = 'academic_management/assessment_confirm_delete.html'
    success_url = reverse_lazy('assessment-list')

class ReportCardListView(LoginRequiredMixin, ListView):
    model = ReportCard
    template_name = 'academic_management/reportcard_list.html'
    context_object_name = 'reportcards'

class ReportCardCreateView(LoginRequiredMixin, CreateView):
    model = ReportCard
    form_class = ReportCardForm
    template_name = 'academic_management/reportcard_form.html'
    success_url = reverse_lazy('reportcard-list')

class ReportCardUpdateView(LoginRequiredMixin, UpdateView):
    model = ReportCard
    form_class = ReportCardForm
    template_name = 'academic_management/reportcard_form.html'
    success_url = reverse_lazy('reportcard-list')

class ReportCardDeleteView(LoginRequiredMixin, DeleteView):
    model = ReportCard
    template_name = 'academic_management/reportcard_confirm_delete.html'
    success_url = reverse_lazy('reportcard-list')

