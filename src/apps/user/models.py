from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# from src.resources import models as resource_models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"

    base_role = Role.ADMIN

    role = models.CharField(max_length=20, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ADMIN)


class Admin(User):
    base_role = User.Role.ADMIN

    admin = AdminManager()

    class Meta:
        proxy = True


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        restults = super().get_queryset(*args, **kwargs)
        return restults.filter(role=User.Role.STUDENT)


class Student(User):
    base_role = User.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.username


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs) -> models.QuerySet:
        results: models.QuerySet = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)


class Teacher(User):
    base_role = User.Role.TEACHER
    teacher = TeacherManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.username


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)


class StudentProfile(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self) -> str:
        return self.user.username + "'s profile"


@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "TEACHER":
        TeacherProfile.objects.create(user=instance)


class TeacherProfile(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    profile_picture = models.ImageField()




    

