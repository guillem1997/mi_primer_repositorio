from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
def anadir(request):
    return render(request, 'anadir.html')
# Create your views here.
