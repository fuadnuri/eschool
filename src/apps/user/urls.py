from django.urls import path, include
from django.contrib.auth import views as auth_views
from src.apps.user import views as user_views
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
        user_views.StudentRegisterationView.as_view(),
        name="student_registration",
    ),
    path(
        "teacher_registration/",
        user_views.TeacherRegistration.as_view(),
        name="teacher_registration",
    ),
    path(
        "profile/",
        login_required(user_views.ProfileView.as_view(), login_url="/login"),
        name="profile",
    ),
]


