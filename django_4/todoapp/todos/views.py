from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Todo app')

def todos(request):
    return(render, 'todos/index.html')