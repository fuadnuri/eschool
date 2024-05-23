from rest_framework.serializers import ModelSerializer 
from people.models import (Adm,Instructor,Student,Moderator)


class AdminSerializer(ModelSerializer):
    class Meta:
        model = Adm
        fields = "__all__"



class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


        
class ModeratorSerializer(ModelSerializer):
    class Meta:
        model = Moderator
        fields = "__all__"

        
        
class InstructortSerializer(ModelSerializer):
    class Meta:
        model = Instructor
        fields = "__all__"

        