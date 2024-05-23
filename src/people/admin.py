from django.contrib import admin
from django.contrib.auth.models import User
from .models import (Adm,Student,Instructor,Moderator)
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Moderator)
admin.site.register(Adm)


