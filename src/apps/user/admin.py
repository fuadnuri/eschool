from django.contrib import admin
from .models import *


@admin.register(Student, Teacher, Admin)
class studentAdmin(admin.ModelAdmin):
    fields = ["username", "email", "first_name", "last_name", "password"]
    list_display = ["username", "email", "first_name", "last_name"]


@admin.register(StudentProfile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ["profile_picture", "user"]
    list_display = ["username", "email", "first_name", "last_name"]

    def username(self, obj):
        username = obj.user.username
        return username

    def first_name(self, obj):
        first_name = obj.user.first_name

        return first_name

    def last_name(self, obj):
        last_name = obj.user.last_name

        return last_name

    def email(self, obj):
        email = obj.user.email

        return email


# Register your models here.
