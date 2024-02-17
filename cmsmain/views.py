from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import *
from .models import *

# Create your views here.


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student
    template_name = 'cmsmain/student_detail.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        context["subjects"] = student.subjects.all()
        return context

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = '/success/'

def my_success_view(request):
    return render(request, 'cmsmain/student_success.html')
