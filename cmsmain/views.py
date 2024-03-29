
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist
import numpy as np

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

@login_required(login_url='auth/login/')
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
            students = Student.objects.all()
            total_students = students.count()
            teachers = Teacher.objects.all()
            total_teachers = teachers.count()
            classes = CourseClass.objects.all()
            total_classes = classes.count()
            context = {'user': user, 'group': group, 'students': students, 'total_students': total_students, 'teachers': teachers, 'total_teachers': total_teachers, 'total_classes': total_classes}
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
    
    
# Search view ----------------------------------
class SearchResultsView(ListView):
    model = Student
    template_name = 'app_student/studentsearch.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Student.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
        return object_list



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
    form_class = ContactForm
    success_url = '/contact_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
    
        student_id = self.kwargs.get('pk')
        if student_id:
            student = Student.objects.get(pk=student_id)
            context['student'] = student
        return context
    
    def form_valid(self, form):
        form.instance.student_id = self.kwargs.get('pk')  # Set the student ID before saving
        return super().form_valid(form)

class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['full_name', 'phone', 'email', 'relationship']
    success_url = '/contact_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = self.get_object()
        context["student"] = contact.student
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
        context["term_end"] = exam.course_class.term.end_date
        context["term_start"] = exam.course_class.term.start_date
        context["class"] = exam.course_class.class_name
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
        context["class"] = test.course_class.class_name
        context["class.id"] = test.course_class.id

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
        assignment = self.get_object()
        context["term_end"] = assignment.term.end_date
        context["term_start"] = assignment.term.start_date
        context["class"] = assignment.course_class.class_name
        context["class.id"] = assignment.course_class.id

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


# CourseClass Views --------------------------------
class CourseClassListView(ListView):
    model = CourseClass
    template_name = 'app_courseclass/courseclass_list.html'


class CourseClassDetailView(DetailView):
    model = CourseClass
    template_name = 'app_courseclass/courseclass_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courseclass = self.get_object()
        context["students"] = courseclass.students.all()
        return context


class CourseClassCreateView(CreateView):
    model = CourseClass
    fields = '__all__'
    success_url = '/courseclass_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context


class CourseClassUpdateView(UpdateView):
    model = CourseClass
    fields = '__all__'
    success_url = '/courseclass_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context


class CourseClassDeleteView(DeleteView):
    model = CourseClass
    template_name = 'app_courseclass/courseclass_confirm_delete.html'
    success_url = reverse_lazy('courseclass_list')


def courseclass_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_courseclass/courseclass_success.html', context)


# Location Views
class LocationListView(ListView):
    model = Location
    template_name = 'app_location/location_list.html'


class LocationDetailView(DetailView):
    model = Location
    template_name = 'app_location/location_detail.html'


class LocationCreateView(CreateView):
    model = Location
    fields = '__all__'
    success_url = '/location_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'create'
        return context


def location_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_location/location_success.html', context)


class LocationUpdateView(UpdateView):
    model = Location
    fields = '__all__'
    success_url = '/location_success/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context


class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'app_location/location_confirm_delete.html'
    success_url = reverse_lazy('location_list')
    
    

# ExamMark --------------------------------------------------------

class ExamMarkListView(ListView):
    model = ExamMark
    template_name = 'app_exammark/exammark_list.html'
    # Optional: sets the name of the context variable
    context_object_name = 'exammark_list'

    def get_queryset(self):
        return super().get_queryset().order_by('exam__name')

    
    
class TeacherExamMarkListView(ListView):
    model = ExamMark
    template_name = 'app_exammark/teacher_exammark_list.html'
    # Optional: sets the name of the context variable
    context_object_name = 'teacher_exammark_list'

    def get_queryset(self):
        # Assuming you have some way to access the logged-in teacher
        # Adjust this according to your user model
        logged_in_teacher = self.request.user.teacher

        # Filter the classes taught by the logged-in teacher
        teacher_classes = logged_in_teacher.classes.all()

        # Fetch all exams associated with the classes taught by the teacher
        teacher_exams = Exam.objects.filter(course_class__in=teacher_classes)

        # Filter ExamMarks based on exams associated with the teacher
        return super().get_queryset().filter(exam__in=teacher_exams).order_by('exam__name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.request.user.teacher
        context['teacher'] = teacher
        return context
    

class ExamMarkDetailView(DetailView):
    model = ExamMark
    template_name = 'app_exammark/exammark_detail.html'


class ExamMarkCreateView(LoginRequiredMixin, CreateView):
    model = ExamMark
    fields = ['exam', 'student', 'mark', 'remark']
    template_name = 'app_exammark/exammark_create.html'
    # Use reverse_lazy for dynamic URL resolution
    success_url = reverse_lazy('exammark_success')

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teacher
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.request.user.teacher
        course_classes = CourseClass.objects.filter(teacher=teacher)
        exams = Exam.objects.filter(course_class__in=course_classes)
        context['exams'] = exams
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Dynamically adjust queryset of 'student' field based on selected exam
        exam_id = self.request.POST.get('exam')
        if exam_id:
            exam = get_object_or_404(Exam, pk=exam_id)
            students = exam.course_class.students.all()
            form.fields['student'].queryset = students
        else:
            # Empty queryset by default
            form.fields['student'].queryset = Student.objects.none()
        return form


def fetch_students(request):
    if request.method == 'GET' and 'exam_id' in request.GET:
        exam_id = request.GET.get('exam_id')
        students = Student.objects.filter(classes__exams__id=exam_id)
        students_data = [
            {'id': student.id, 'full_name': f"{student.first_name} {student.last_name}"} for student in students]
        return JsonResponse(students_data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)




def exammark_success_view(request):
    user = request.user
    group_list = [group.name for group in user.groups.all()]
    group = group_list[0]
    context = {'user': user, 'group': group}
    return render(request, 'app_exammark/exammark_success.html', context)


class ExamMarkUpdateView(UpdateView):
    model = ExamMark
    fields = ['student', 'mark', 'remark']  # Fields to display in the form
    success_url = '/exammark_success/'  # Redirect URL after successful update

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        try:
            # Filter students based on the associated exam
            exam_id = self.object.exam_id
            form.fields['student'].queryset = form.fields['student'].queryset.filter(
                exammarks__exam_id=exam_id)
        except AttributeError as e:
            # Handle attribute error
            print(f"AttributeError: {e}")
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation'] = 'update'
        return context


class ExamMarkDeleteView(DeleteView):
    model = ExamMark
    template_name = 'app_exammark/exammark_confirm_delete.html'
    success_url = reverse_lazy('exammark_list')
    
class TeacherExamMarkDeleteView(DeleteView):
    model = ExamMark
    template_name = 'app_teacher/teacher_exammark_confirm_delete.html'
    success_url = reverse_lazy('teacher_exammark_list')


def exam_results(request):
    if request.method == 'POST':
        exam_id = request.POST.get('exam_id')
        selected_exam = Exam.objects.get(pk=exam_id)
        selected_class = selected_exam.course_class
        exam_marks = ExamMark.objects.filter(exam=selected_exam)
        context = {'selected_exam': selected_exam, 'exam_marks': exam_marks, 'selected_class': selected_class}
        return render(request, 'app_exammark/exam_results.html', context)
    else:
        # Assuming you have implemented user authentication and each teacher has a corresponding user
        teacher = request.user.teacher
        course_classes = teacher.classes.all()
        exams = Exam.objects.filter(course_class__in=course_classes)
        return render(request, 'app_exammark/exam_selection.html', {'exams': exams})


def class_results(request):
    if request.method == 'POST':
        course_class_id = request.POST.get('course_class_id')
        selected_class = CourseClass.objects.get(pk=course_class_id)
        students = selected_class.students.all()
        teacher = request.user.teacher
        exams = selected_class.exams.all()
        
        exam_marks_dict = {}

        for exam in exams:
            # Initialize an empty list for each exam
            exam_marks_dict[exam] = []

        for student in students:
            for exam in exams:
                exam_mark = ExamMark.objects.filter(
                    student=student, exam=exam).first()

                if exam_mark:
                    mark = int(exam_mark.mark)
                    exam_marks_dict[exam].append(mark)

                else:
                    exam_marks_dict[exam].append(0)

        # Initialize the 'Total' list with zeros
        total_marks = [0] * len(next(iter(exam_marks_dict.values())))

        # Sum the marks for each student
        for marks in exam_marks_dict.values():
            total_marks = [total_marks[i] + marks[i] for i in range(len(marks))]

        # Add the total marks to the 'Total' key
        exam_marks_dict['Total'] = total_marks
            
        
        # Reverse the marks in the lists in exam_marks_dict so they pop in right order in the template
        reverse_marks_dict = {key: value[::-1] for key, value in exam_marks_dict.items()}

        context = {
            'selected_class': selected_class,
            'students': students,
            'teacher': teacher,
            'exams': exams,
            'reverse_marks_dict': reverse_marks_dict,  # Pass the dictionary to the template
        }
        return render(request, 'app_exammark/class_results.html', context)

    else:
        teacher = request.user.teacher
        course_classes = teacher.classes.all()
        exams = Exam.objects.filter(course_class__in=course_classes)
        return render(request, 'app_exammark/class_selection.html', {'exams': exams, 'course_classes': course_classes})




# Exam marks view for students
@login_required
def exam_marks_view(request):
    form = ExamMarksFilterForm(request.POST or None)
    exam_marks = ExamMark.objects.filter(student=request.user.student)
    student = request.user.student

    if request.method == 'POST':
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            course_class = form.cleaned_data.get('course_class')
            exam = form.cleaned_data.get('exam')

            if subject:
                exam_marks = exam_marks.filter(
                    exam__course_class__subject=subject)
            if course_class:
                exam_marks = exam_marks.filter(exam__course_class=course_class)
            if exam:
                exam_marks = exam_marks.filter(exam=exam)

    context = {
        'form': form,
        'exam_marks': exam_marks,
        'student': student
    }
    return render(request, 'app_student/exam_marks.html', context)
