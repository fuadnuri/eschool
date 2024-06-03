from django.db import models 
from django.utils import timezone
from src.apps.user import models as user_models


class Course(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(to=user_models.Teacher,on_delete=models.CASCADE)
    descrtiption = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="course.jpg",upload_to='courses_pics')
    def __str__(self) -> str:
        return self.title
    

class CourseFile(models.Model):
    course = models.ForeignKey(to=Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class CourseSubscription(models.Model):
    user = models.ForeignKey(to=user_models.Student, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course ,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username + self.course.title 