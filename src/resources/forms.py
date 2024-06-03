from django import forms
class SearchCourse(forms.Form):
    query = forms.CharField(
     help_text="Search for any courses on the site.")