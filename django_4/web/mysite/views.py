from django.shortcuts import render, HttpResponse
from .models import certificates
# Create your views here.

def home(request):
    return HttpResponse('Hello Stan')

def cert(request):
    items = certificates.objects.all()

    return render(request, 'mysite/index.html', {'certificate':items})