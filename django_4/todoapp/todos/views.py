from django.shortcuts import render, HttpResponse
from .models import todos
# Create your views here.
def home(request):
    return HttpResponse('Welcome to Todo app')

def todoapp(request):
    item = todos.objects.all()
    return render(request, 'todos/index.html', {'todos':item})