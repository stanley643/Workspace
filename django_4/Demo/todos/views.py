from django.shortcuts import render, HttpResponse
from .models import todo

# Create your views here.
def home(request):
    item = todo.objects.all()
    return render(request, 'todos/home.html', {"todo":item})