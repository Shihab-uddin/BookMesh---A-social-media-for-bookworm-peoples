from django.urls import path
from .views import postListView, postCreateView
from . import views


urlpatterns = [
    path('', postListView.as_view(), name='blog_home'),
    path('create/', postCreateView.as_view(), name='create'),
    path('profile/', views.profile_view, name='blog_profile')

]