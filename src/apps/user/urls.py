from django.urls import path, include
from django.contrib.auth import views as auth_views
from src.apps.user.views import students as students_view,teachers as teachers_view
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="user/logout.html"),
        name="logout",
    ),
    path(
        "student_registration/",
        students_view.StudentRegisterationView.as_view(),
        name="student_registration",
    ),
    path(
        "teacher_registration/",
        teachers_view.TeacherRegistrationView.as_view(),
        name="teacher_registration",
    ),
    path(
        "profile/",
        login_required(students_view.ProfileView.as_view(), login_url="/login"),
        name="profile",
    ),
    path('tdashboard/',
         login_required(teachers_view.Dashboard.as_view(),login_url="login"),
         name='teacher-dashboard'),
    
]
