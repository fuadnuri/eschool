from django.shortcuts import redirect,render
from django.views import View 
from django.contrib import messages
from src.apps.user.forms import students as student_forms
from src.resources import models as resource_models
from src.apps.user import models as user_models


# student StudentRegisterationView
class StudentRegisterationView(View):
    form_class = student_forms.StudentRegistrationForm
    template_name = "student/student_registration.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = student_forms.StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'hello {form.cleaned_data.get("username")}')
            return redirect("login")
        else:
            return render(
                request, self.template_name, {"form": self.form_class}
            )


# view courses listview
class MyCoursesView(View):
    context = {}
    template_name = "resources/my_courses.html"

    def get(self, request, username):

        reg = resource_models.CourseSubscription.objects.filter(
            user=user_models.Student.objects.get(username=username)
        )
        courses = [resource_models.Course.objects.get(id=r.course.id) for r in reg]
        self.context["courses"] = courses
        return render(request, template_name=self.template_name, context=self.context)



# student profile view and edit view 
class ProfileView(View):
    template_name = "user/profile.html"

    def get(self, request):
        u_form = student_forms.StudentChangeForm(instance=request.user)
        p_form = student_forms.StudentProfileChangeForm(instance=request.user.studentprofile)
        context = {
            "u_form": u_form,
            "p_form": p_form,
        }
        # user = get_object_or_404(Student,username=username)
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        u_form = student_forms.StudentChangeForm(request.POST, instance=request.user)
        p_form = student_forms.StudentProfileChangeForm(
            request.POST, request.FILES, instance=request.user.studentprofile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")


# dashboard view for authenticated students
class Dashboard(View):
    template_name = "user/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request)

