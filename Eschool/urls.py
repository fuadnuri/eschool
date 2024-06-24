from django.contrib import admin
from django.urls import path, include
from src.apps.user.views import (anonymous as user_views,students as student_view,teachers as teachers_view, admin_view as admin_views)
from Eschool.settings import base
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", user_views.Home.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("admin-dashboard/",admin_views.AdminDashboardView.as_view(),name="admin-view"),
    path("admin-dashboard/course",admin_views.AdminDashBoardViewCourseEdit.as_view(),name='admin-courses'),
    path("admin-dashboard/users",admin_views.AdminCrud.as_view(),name="admin-teacher"),
    path("about", user_views.About.as_view(), name="about"),
    path("user/", include("src.apps.user.urls")),
    path("resource/", include("src.resources.urls"), name="resources"),
    path(
        "my-courses/<slug:username>",
        login_required(student_view.MyCoursesView.as_view(), login_url="login"),
        name="my-courses",
    ),
    path("create_course/",login_required(teachers_view.CourseCreationView.as_view(),login_url="/login"),name="create-course")
]
if base.DEBUG:
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)


handler404 = "src.resources.views.custom404"
