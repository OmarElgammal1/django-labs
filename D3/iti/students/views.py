from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_students(request):
    students = [
        {'id': 1, 'name': 'Ahmed', 'age': 20, 'track': 'AI'},
        {'id': 2, 'name': 'Ali', 'age': 21, 'track': 'OS'},
        {'id': 3, 'name': 'Omar', 'age': 22, 'track': 'Embedded'},
    ]

    track = request.GET.get('track')
    if track:
        students = [student for student in students if student['track'] == track]

    context = {
        'students': students
    }
    return render(request, 'base.html', context)


def student_details(request, id):
    return HttpResponse(f'welcome {id}')