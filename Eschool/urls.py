from django.contrib import admin
from django.urls import path, include
from src.apps.user import views as user_views
from Eschool.settings import base
from django.conf.urls.static import static
urlpatterns = [
    path("", user_views.Home.as_view(), name="home"),
    path("about", user_views.About.as_view(), name="about"),
    path("admin/", admin.site.urls),
    path("user/", include("src.apps.user.urls")),
    path("resource/",include("src.resources.urls"),name='resources'),
    
]
if base.DEBUG:
    urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)


handler404 = 'src.resources.views.custom404'