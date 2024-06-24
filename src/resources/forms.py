from django import forms
from src.resources import models as resources_model


class SearchCourseForm(forms.Form):
    query = forms.CharField(help_text="Search for any courses on the site.")


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = resources_model.Course
        fields = ["title", "descrtiption", "image", "created_by"]
