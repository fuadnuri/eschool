from django.views import View
from django.shortcuts import render,redirect
from src.resources.models import Course
from src.apps.user.models import Teacher,Student


from django.views.generic.list import ListView 
from django.views.generic.edit import DeleteView


class AdminDashboardView(View):
    template_name = "admin/dashboard.html"
    context ={}
    def post(self,request):
        return 
    def get(self,request):
        # if request.user.role =="Admin":
        return render(request,template_name=self.template_name,context=self.context)
        # return 

class AdminDashBoardViewCourseEdit(View):
    template_name = 'admin/courses.html'
    context = {}

    def get(self,request):
        queryset= Course.objects.all()
        self.context['courses']=queryset
        return render(request,template_name=self.template_name,context=self.context)
    

class AdminCrud(View):
    template_name = "admin/admin_crud.html"
    context_super_user = {}
    context={}

    def get(self,request):
        # if request.user.is_superuser:
        #     return render(request, template_name=self.template_name,context=self.context_super_user)
        self.context['users'] = Teacher.objects.all()
        return render(request,template_name=self.template_name,context=self.context)
    
