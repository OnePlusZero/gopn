from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    return render(request, 'pews/index.html', {})

def position_list(request):
    return render(request, 'pews/indux.html', {})

def about(request):
    return render(request, 'pews/about.html', {})

def gal(request):
    return render(request, 'pews/gal.html')

def howtous(request):
    return render(request, 'pews/howtous.html')

def test(request):
    return render(request,'pews/test.html')

def doc(request):
    return render(request,'pews/doc.html')

def news(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,"pews/news.html",{'posts': posts})
