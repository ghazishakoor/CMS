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
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    
    return render(request, 'app_student/student_page.html', context)


def TeacherPage(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}

    return render(request, 'app_teacher/teacher_page.html', context)


def AdminPage(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}

    return render(request, 'cmsmain/admin_page.html', context)


def custom_redirect(request):
    user = request.user
    if user.is_authenticated:
        if user.groups.filter(name='student').exists():
            group = 'student'
            student = Student.objects.get(user=user)
            subjects = student.subjects.all()
            context = {'user': user, 'group': group, 'student': student, 'subjects': subjects}
            return render(request, 'app_student/student_page.html/', context)

        elif user.groups.filter(name='teacher').exists():
            group = 'teacher'
            teacher = Teacher.objects.get(user=user)
            subjects = teacher.subjects.all()
            context = {'user': user, 'group': group, 'teacher': teacher, 'subjects': subjects}
            return render(request, 'app_teacher/teacher_page.html/', context)
        
        elif user.groups.filter(name='admin').exists():
            group = 'admin'
            context = {'user': user, 'group': group}
            return render(request, 'cmsmain/admin_page.html/', context)
        # Add more conditions for other user groups as needed
        
    return render(request, 'cmsmain/home.html/')
    

# Student Views ---------------------------
class StudentListView(ListView):
    model = Student
    template_name = 'app_student/student_list.html'
    paginate_by = 6

class StudentDetailView(DetailView):
    model = Student
    template_name = 'app_student/student_detail.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        contact = Contact.objects.filter(student=student).first()
        context["contact"] = contact
        context["subjects"] = student.subjects.all()
        return context

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentAssignmentForm
    success_url = '/student_success/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context

def student_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_student/student_success.html', context)


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
    template_name = 'app_student/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')



# Teacher Views --------------------------------
class TeacherListView(ListView):
    model = Teacher
    template_name = 'app_teacher/teacher_list.html'
    paginate_by = 8
    
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'app_teacher/teacher_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        context["subjects"] = teacher.subjects.all()
        return context

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherAssignmentForm
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
    template_name = 'app_teacher/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')
    
def teacher_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_teacher/teacher_success.html', context)



# Subject Views ---------------------------
class SubjectListView(ListView):
    model = Subject
    template_name = 'app_subject/subject_list.html'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'app_subject/subject_detail.html'

class SubjectCreateView(CreateView):
    model = Subject
    fields = '__all__'
    success_url = '/subject_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context


def subject_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_subject/subject_success.html', context)

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = '__all__'
    success_url = '/subject_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'app_subject/subject_confirm_delete.html'
    success_url = reverse_lazy('subject_list')



# Contact Views -------------------------
class ContactDetailView(DetailView):
    model = Contact
    template_name = 'app_contact/contact_detail.html'


class ContactCreateView(CreateView):
    model = Contact
    fields = '__all__'
    success_url = '/contact_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context

class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'
    success_url = '/contact_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'app_contact/contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')


def contact_success_view(request):
    return render(request, 'app_contact/contact_success.html')



# Exam Views ---------------
class ExamListView(ListView):
    model = Exam
    template_name = 'app_assessments/exam_list.html'

class ExamDetailView(DetailView):
    model = Exam
    template_name = 'app_assessments/exam_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exam = self.get_object()
        context["term_end"] = exam.term.end_date
        context["term_start"] = exam.term.start_date
        return context

class ExamCreateView(CreateView):
    model = Exam
    fields = '__all__'
    success_url = '/exam_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context


def exam_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_assessments/exam_success.html', context)


class ExamUpdateView(UpdateView):
    model = Exam
    fields = '__all__'
    success_url = '/exam_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context


class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'app_assessments/exam_confirm_delete.html'
    success_url = reverse_lazy('exam_list')



# Test Views ----------------------
class TestListView(ListView):
    model = Test
    template_name = 'app_assessments/test_list.html'

class TestDetailView(DetailView):
    model = Test
    template_name = 'app_assessments/test_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = self.get_object()
        context["term_end"] = test.term.end_date
        context["term_start"] = test.term.start_date
        return context

class TestCreateView(CreateView):
    model = Test
    fields = '__all__'
    success_url = '/test_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context


def test_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_assessments/test_success.html', context)

class TestUpdateView(UpdateView):
    model = Test
    fields = '__all__'
    success_url = '/test_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context

class TestDeleteView(DeleteView):
    model = Test
    template_name = 'app_assessments/test_confirm_delete.html'
    success_url = reverse_lazy('test_list')


# Assignmnet Views
class AssignmentListView(ListView):
    model = Assignment
    template_name = 'app_assessments/assignment_list.html'


class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'app_assessments/assignment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = self.get_object()
        context["term_end"] = test.term.end_date
        context["term_start"] = test.term.start_date
        return context


class AssignmentCreateView(CreateView):
    model = Assignment
    fields = '__all__'
    success_url = '/assignment_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context


def assignment_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_assessments/assignment_success.html', context)


class AssignmentUpdateView(UpdateView):
    model = Assignment
    fields = '__all__'
    success_url = '/assignment_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context


class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = 'app_assessments/assignment_confirm_delete.html'
    success_url = reverse_lazy('assignment_list')
    

# Term Views
class TermListView(ListView):
    model = Term
    template_name = 'app_term/term_list.html'


class TermDetailView(DetailView):
    model = Term
    template_name = 'app_term/term_detail.html'



class TermCreateView(CreateView):
    model = Term
    fields = '__all__'
    success_url = '/term_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context


def term_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_term/term_success.html', context)


class TermUpdateView(UpdateView):
    model = Term
    fields = '__all__'
    success_url = '/term_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context


class TermDeleteView(DeleteView):
    model = Assignment
    template_name = 'app_term/term_confirm_delete.html'
    success_url = reverse_lazy('term_list')
