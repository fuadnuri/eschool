from django import forms
from django.contrib.auth import forms as auth_form
from ..models import Student, StudentProfile


class StudentRegistrationForm(auth_form.UserCreationForm):

    email = forms.EmailField()

    class Meta(auth_form.UserCreationForm.Meta):
        model = Student
        fields = ["username", "email", "password1", "password2"]


class StudentChangeForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Student
        fields = ["email", "first_name", "last_name"]


class StudentProfileChangeForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ["profile_picture"]