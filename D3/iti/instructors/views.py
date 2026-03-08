from django.shortcuts import render, get_object_or_404
from .models import Instructor

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors/list.html', {'instructors': instructors})

def instructor_courses(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    courses = instructor.courses.all()
    return render(request, 'instructors/courses.html', {'instructor': instructor, 'courses': courses})
