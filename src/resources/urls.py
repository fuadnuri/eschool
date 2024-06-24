from django.urls import path
from . import views as course_views

urlpatterns = [
    path("", course_views.Course.as_view(), name="course-list-view"),
    path(
        "course/<int:pk>/",
        course_views.CourseDetailView.as_view(),
        name="course-detail-view",
    ),
]
