from django.shortcuts import render
from django.views import View
from src.resources import models as resource_models

from django.contrib.auth import forms


class Home(View):
    template_name = "user/home.html"

    def get(self, request):
        course_list = resource_models.Course.objects.all()
        context = {"courses": course_list}
        return render(request, "user/home.html", context=context)


class About(View):
    template_name = "user/about.html"

    def get(self, request):

        return render(request, self.template_name)








# course creation view 
# course form

