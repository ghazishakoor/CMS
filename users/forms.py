from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group  # Import the Group model
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.filter(
        name__in=['student', 'teacher']), empty_label=None, required=True)
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2', 'group']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        group = self.cleaned_data['group']
        if commit:
            user.save()
            user.groups.add(group)  # Assign the selected group to the user
        return user