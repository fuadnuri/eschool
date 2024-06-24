from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . import models as course_models
from django.contrib import messages

from . import forms as resources_forms
from django.core.paginator import Paginator

# from django.http.response import


class Course(View):
    template_name = "resources/courses.html"
    context = {}

    search_form = resources_forms.SearchCourseForm()

    def get(self, request):

        queryset = course_models.Course.objects.all()
        paginator = Paginator(queryset,6)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    # return render(request, "list.html", {"page_obj": page_obj})
        self.context["form"] = self.search_form
        self.context["courses"] = page_obj
        self.context['page_num'] = page_obj.number
        self.context['total_page']=paginator.num_pages
        self.context['has_next']= 'active' if page_obj.has_next else "disabled"
        self.context['has_previous']= 'active' if page_obj.has_previous else "disabled"
        return render(request, template_name=self.template_name, context=self.context)

    def post(self, request):
        search_form = resources_forms.SearchCourseForm(request.POST)
        # messages.error(request, f'invalid query {search_form.get("query")}')
        if search_form.is_valid():
            search_key = request.POST["query"]
            queryset = course_models.Course.objects.filter(
                descrtiption__contains=search_key
            )
            self.context["courses"] = queryset
            self.context["form"] = self.search_form
            return render(request, self.template_name, self.context)

        messages.error(request, f"invalid query {request.POST('query')}")
        # return redirect('courses')


# Create your views here.


class CourseDetailView(View):
    template_name = "resources/course_detail.html"
    page_404 = "user/page-404.html"

    def get(self, request, pk):
        # course = get_object_or_404(course_models.Course,id=pk)

        course = get_object_or_404(course_models.Course, pk=pk)
        # course = get_object_or_404(course_models.Course,id=pk)
        if course:
            try:
                course_file = course_models.CourseFile.objects.filter(course=course)
                context = {"course": course, "course_file": course_file}
                return render(
                    request, template_name=self.template_name, context=context
                )

            except:
                context = {"course": course, "course_file": None}

            return render(
                request,
                template_name=self.template_name,
                context={"course": course, "course_res": None},
            )
        else:
            return render(request, template_name=self.page_404)

    def post(self, request):
        user = request.user
        course_id = request.POST.get("value")
        course = Course.objects.get(id=course_id)
        course_file = course_models.CourseFile.objects.get(user=user, course=course)
        if course_file.DoesNotExist:
            new_course_file = course_models.CourseFile(user=user, course=course)
            new_course_file.save()
            messages.success(request, "succesfully subscribed to course")
            return redirect("my-courses", user.username)

        messages.error(request, "you've already registered to the course!")
        return redirect("home")


def custom404(request, exception):
    template_name = "user/page-404.html"
    return render(request, template_name=template_name, status=404)
