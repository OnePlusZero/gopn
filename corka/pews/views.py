from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    return render(request, 'pews/index.html', {})
    
def position_list(request):
    return render(request, 'pews/indux.html', {})

def about(request):
    return render(request, 'pews/about.html', {})

def gal(request):
    return render(request, 'pews/gal.html')