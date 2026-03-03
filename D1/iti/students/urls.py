from django.urls import path, include
from students.views import test, test2

# http://localhost:8000/students
urlpatterns = [
    path('', test),
    path('<str:id>', test2),
]