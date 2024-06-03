from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from . import models as course_models

from .  import forms as resources_forms
# from django.http.response import

class Course(View):
    template_name = "resources/courses.html"
    context = {}
    
    def get(self,request):
        
        queryset = course_models.Course.objects.all()

        search_form = resources_forms.SearchCourse()
        self.context['form'] = search_form
        self.context['courses']=queryset
        return render(request, template_name= self.template_name, context=self.context)
    def post(self,request):
        search_form = resources_forms.SearchCourseForm(request.post)
        if search_form.is_valid():
            queryset= course_models.Course.objects.filter(discription_contains=search_form.query)
            self.context['courses']=queryset
            return render(request,self.template_name,self.context)
        return redirect('courses')
# Create your views here.


class CourseDetailView(View):
    template_name = "resources/course_detail.html"
    page_404 = 'user/page-404.html'

    def get(self,request,pk):
        # course = get_object_or_404(course_models.Course,id=pk)
        
        course = get_object_or_404(course_models.Course,pk=pk)
        # course = get_object_or_404(course_models.Course,id=pk)
        if course.DoesNotExist:
            return render(request, template_name=self.page_404)
        else:
            try:
                course_file = course_models.CourseFile.objects.get(course=course) 
                context = {"course":course,"course_file":course_file}
                return render(request, template_name = self.template_name, context=context)
            
            except:
                context = {"course":course,"course_file":None}

            return render(request,template_name=self.template_name,context={"course":course,"course_res":None})
        
        
def custom404(request,exception):
    template_name = "user/page-404.html"
    return render(request,template_name=template_name,status=404)






