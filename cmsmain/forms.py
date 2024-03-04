from django import forms
from .models import *
from django.contrib.auth.models import User, Group


class StudentAssignmentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'subjects', 'student_number', 'first_name', 'last_name', 'phone', 'date_of_birth', 'nationality', 'passport_number', 'email', 'enrolment_date', 'picture']

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


class TeacherAssignmentForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'subjects', 'first_name', 'last_name', 'phone', 'email', 'date_joined']

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



class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['full_name', 'phone', 'email', 'relationship']


