from django.urls import path
from . import views

app_name = 'instructors'

urlpatterns = [
    path('', views.instructor_list, name='list'),
    path('<int:instructor_id>/courses/', views.instructor_courses, name='courses'),
]
