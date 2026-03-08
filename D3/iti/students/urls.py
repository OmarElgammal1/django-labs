from django.urls import path, include
from students.views import list_students, student_details

# http://localhost:8000/students
urlpatterns = [
    path('', list_students),
    path('<str:id>', student_details, name='std_details'),
]