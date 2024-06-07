from django import forms
from .models import *
from django.contrib.auth.models import User, Group

class DateInput(forms.DateInput):
    input_type = 'date'


class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = '__all__'
        widgets = {
            'start_date': DateInput,
            'end_date': DateInput
        }


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        widgets = {
            'date': DateInput
        }



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput,
            'enrolment_date': DateInput
        }


class StudentAssignmentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'subjects', 'student_number', 'first_name', 'last_name', 'phone', 'date_of_birth', 'nationality', 'passport_number', 'email', 'enrolment_date', 'picture']
        widgets = {
            'date_of_birth': DateInput,
            'enrolment_date': DateInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filter users to exclude those already assigned to a person and superusers
        assigned_users = set(Student.objects.values_list('user_id', flat=True)) | \
            set(Teacher.objects.values_list('user_id', flat=True))
        
        # Get users who are members of the admin group
        # Replace 'admin' with the actual name of your admin group
        admin_group = Group.objects.get(name='admin')
        admin_users = admin_group.user_set.values_list('id', flat=True)
        
        self.fields['user'].queryset = User.objects.filter(
            is_superuser=False
        ).exclude(
            id__in=assigned_users
        ).exclude(
            id__in=admin_users
        )


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'date_joined': DateInput
        }

class TeacherAssignmentForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subjects', 'first_name', 'last_name', 'phone', 'email', 'date_joined']
        widgets = {
            'date_joined': DateInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filter users to exclude those already assigned to a person and superusers
        assigned_users = set(Student.objects.values_list('user_id', flat=True)) | \
            set(Teacher.objects.values_list('user_id', flat=True))
        
        # Get users who are members of the admin group
        # Replace 'admin' with the actual name of your admin group
        admin_group = Group.objects.get(name='admin')
        admin_users = admin_group.user_set.values_list('id', flat=True)
        
        self.fields['user'].queryset = User.objects.filter(
            is_superuser=False
        ).exclude(
            id__in=assigned_users
        ).exclude(
            id__in=admin_users
        )


class ExamMarksFilterForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(
    ), required=False, widget=forms.Select(attrs={'class': 'form-field'}))
    course_class = forms.ModelChoiceField(queryset=CourseClass.objects.all(), required=False)
    exam = forms.ModelChoiceField(queryset=Exam.objects.all(), required=False)


class StudentSubjectMarksFilterForm(forms.Form):
    subject = forms.ModelChoiceField(
        queryset=None,
        required=False,
        widget=forms.Select(attrs={'class': 'form-field'})
    )

    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)
        super(StudentSubjectMarksFilterForm, self).__init__(*args, **kwargs)
        if student:
            self.fields['subject'].queryset = Subject.objects.filter(
                classes__in=student.classes.all()).distinct()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone', 'email', 'relationship']


