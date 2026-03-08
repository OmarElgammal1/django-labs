from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('<int:course_id>/students/', views.course_students, name='students'),
]
