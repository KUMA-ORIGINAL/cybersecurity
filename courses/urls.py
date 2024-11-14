from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('courses/', views.index, name='index'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]