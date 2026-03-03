from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse('welcome')


def test2(request, id):
    return HttpResponse(f'welcome {id}')