from django.contrib import admin
from . import models as course_models 
admin.site.register(course_models.Course)
admin.site.register(course_models.CourseFile)