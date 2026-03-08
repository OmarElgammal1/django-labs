from django.shortcuts import render, get_object_or_404
from .models import Course

def course_students(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = course.students.all()
    return render(request, 'courses/students.html', {'course': course, 'students': students})