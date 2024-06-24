from django.shortcuts import redirect,render
from django.contrib import messages 
from src.apps.user import models as user_models 
from src.resources import models as resources_models 
from src.resources import forms as resources_form
from django.views import View
from ..forms import teachers as teacher_forms

# teachers home page 
class Dashboard(View):
    template_name = "teacher/dashboard.html"
    forms = {}
    context = {}
    
    def get(self,request):
        course = resources_models.Course.objects.all()[:3]
        self.context['courses']=course
        return render(request, template_name=self.template_name,context =self.context) 

    def post(self,request):
        pass




class TeacherRegistrationView(View):
    form_class = teacher_forms.TeacherCreationForm
    template_name = "teacher/teacher_registration.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = teacher_forms.UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("username"))
        return redirect("login")


class CourseCreationView(View):
    template_name = "resources/create_course.html"
    course_creation_form = resources_form.CourseCreationForm
    context = {}
    def get(self, request):
        if( request.user.role=="TEACHER"):
            self.context["course_form"] = self.course_creation_form()
            return render(request, template_name=self.template_name, context=self.context)
        messages.error(request,"permission denied!")
        return redirect("my-courses" ,request.user.username)
    
    
    def post(self, request):
        if request.user.role =="TEACHER":
            course_data = resources_form.CourseCreationForm(request.POST,request.FILES)

            if course_data.is_valid():
                course_data.save()
                messages.success(request,"you've success fully created a new course")
                return redirect('create-course')
            self.context['course_form']= self.course_creation_form()
            return render(request,template_name=self.template_name,content_type=self.context)
        messages.error(request,"permission denied!")
        return redirect("my-courses",request.user.username)





