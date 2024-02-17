from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import *
from .models import *

# Create your views here.


class StudentListView(ListView):
    model = Student
    paginate_by = 4

class StudentDetailView(DetailView):
    model = Student
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        context["subjects"] = student.subjects.all()
        return context

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = '/student_success/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context

def student_success_view(request):
    return render(request, 'cmsmain/student_success.html')


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = '/student_success/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')


class TeacherListView(ListView):
    model = Teacher
    paginate_by = 8
    
class TeacherDetailView(DetailView):
    model = Teacher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        context["subjects"] = teacher.subjects.all()
        return context

class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = '/teacher_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = '/teacher_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher_list')


def teacher_success_view(request):
    return render(request, 'cmsmain/teacher_success.html')
