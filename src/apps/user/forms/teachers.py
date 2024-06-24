from django import forms
from ..models import (Teacher,TeacherProfile)
from django.contrib.auth import forms as auth_form



class TeacherCreationForm(auth_form.UserCreationForm):

    email = forms.EmailField()

    class Meta(auth_form.UserCreationForm.Meta):
        model = Teacher
        fields = ["username", "email", "password1", "password2"]


class TeacherChangeForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = ["email", "first_name", "last_name"]


class TeacherProfileChangeForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ["profile_picture"]