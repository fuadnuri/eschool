from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from src.resources import models as resource_models
from django.core.paginator import Paginator


# Create your views here.
from .forms import StudentRegistrationForm, StudentChangeForm, StudentProfileChangeForm
from django.contrib.auth import forms



class Home(View):
    template_name = "user/home.html"
    def get(self, request):
        course_list = resource_models.Course.objects.all()
        context = {"courses": course_list}
        return render(request, "user/home.html",context=context)


class About(View):
    template_name = "user/about.html"

    def get(self, request):

        return render(request, self.template_name)


class Dashboard(View):
    template_name = "user/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request)


class StudentRegisterationView(View):
    form_class = StudentRegistrationForm
    template_name = "user/student_registration.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get("username"))
            messages.success(request, f'hello {form.cleaned_data.get("username")}')
            return redirect("login")
        else:
            return render(
                request, self.template_name, {"form": StudentRegistrationForm}
            )


class TeacherRegistration(View):
    form_class = forms.UserCreationForm
    template_name = "user/teacher_registration.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("username"))
        return redirect("login")





class ProfileView(View):
    template_name = "user/profile.html"

    def get(self, request):
        u_form = StudentChangeForm(instance=request.user)
        p_form = StudentProfileChangeForm(instance=request.user.studentprofile)
        context = {
            "u_form": u_form,
            "p_form": p_form,
        }
        # user = get_object_or_404(Student,username=username)
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        u_form = StudentChangeForm(request.POST, instance=request.user)
        p_form = StudentProfileChangeForm(
            request.POST, request.FILES, instance=request.user.studentprofile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")

