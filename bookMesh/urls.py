"""bookMesh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', user_views.register_view, name='signup'),
    path('profile/', user_views.profile_view, name='profile'),
    path('editprofile/', user_views.profilesettings_view, name='editprofile'),


    path('login/', auth_views.LoginView.as_view(template_name='users/Login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)