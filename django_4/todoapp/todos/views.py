from django.shortcuts import render, HttpResponse
from .models import todos
# Create your views here.
def home(request):
    return HttpResponse('Welcome to Todo app')

def todos(request):
    items = todos.objects.all()
    return(render, 'todos/index.html', 'todos':items)