from django.db import models
from django.utils import timezone
from people.models import Student,Instructor

# Create your models here.

class Course:
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class CourseAssesment(models.Models):
    title = models.CharField(max_length=256)
    detail = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class CourseSubscription(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_Status = models.CharField(max_length=50,default="Started")
    sub_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.student.first_name + self.course.name
    

class CourseFileLink(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resourse_link = models.TextField()


class CourseAssesmentSolutionLink(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    CourseAssesment = models.OneToOneField(course, on_delete=models.CASCADE)
    solution_link = models.TextField()


