from django.shortcuts import render
import uuid
# Create your views here.
def index(request):
    return render(request, 'shortner/index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]