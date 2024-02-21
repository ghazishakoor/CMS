from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

# Create your views here.

class HomeView(TemplateView):
    template_name = "cmsmain/home.html"

def StudentPage(request):
    user = request.user
    user_groups = user.groups.all()
    user_group = ''
    for group in user_groups:
        user_group = group
    
    context = {'user': user, 'group': user_group}
    
    return render(request, 'cmsmain/student_landing_page.html', context)


def TeacherPage(request):
    user = request.user
    user_groups = user.groups.all()
    user_group = ''
    for group in user_groups:
        user_group = group

    context = {'user': user, 'group': user_group}

    return render(request, 'cmsmain/teacher_landing_page.html', context)


def AdminPage(request):
    user = request.user
    user_groups = user.groups.all()
    user_group = ''
    for group in user_groups:
        user_group = group

    context = {'user': user, 'group': user_group}

    return render(request, 'cmsmain/admin_landing_page.html', context)


def custom_redirect(request):
    user = request.user
    if user.is_authenticated:
        if user.groups.filter(name='student').exists():
            group = 'student'
            context = {'user': user, 'group': group}
            return render(request, 'cmsmain/student_page.html/', context)

        elif user.groups.filter(name='teacher').exists():
            group = 'teacher'
            context = {'user': user, 'group': group}
            return render(request, 'cmsmain/teacher_page.html/', context)
        
        elif user.groups.filter(name='admin').exists():
            group = 'admin'
            context = {'user': user, 'group': group}
            return render(request, 'cmsmain/teacher_page.html/', context)
        # Add more conditions for other user groups as needed
        
    return render(request, 'cmsmain/home.html/')
    


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
