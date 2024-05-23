from django.db import models

from django.contrib.auth.models import User

class Adm(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField("pp")

    def __str__(self) -> str:
        return self.user.first_name
    

class Student(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField("stud-pp")

    def __str__(self) -> str:
        return self.user.first_name
    


class Instructor(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField("Inst-pp")

    def __str__(self) -> str:
        return self.user.first_name

class Moderator(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile = models.ImageField('moderator-pp') 

    def __str__(self) -> str:
        return self.user.first_name
