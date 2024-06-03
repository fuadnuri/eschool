from rest_framework.serializers import ModelSerializer

from resources.models import (
    Course,
    CourseAssesment,
    CourseAssesmentSolutionLink,
    CourseFileLink,
    CourseSubscription,
)


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseAssesmentSerializer(ModelSerializer):
    class Meta:
        model = CourseAssesment
        fields = "__all__"


class CourseSubscriptionSerializer(ModelSerializer):

    class Meta:
        model = CourseSubscription
        fields = "__all__"


class CourseFileLink(ModelSerializer):
    class Meta:
        model = CourseFileLink
        fields = "__all__"


class CourseAssesmentSolutionLink(ModelSerializer):
    class Meta:
        model = CourseAssesmentSolutionLink
        fields = "__all__"
