from django.shortcuts import render, get_object_or_404
from .models import Post, NewsList
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
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'pews/test.html', {'posts':posts})

def doc(request):
    return render(request,'pews/doc.html')

def news(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,"pews/news.html",{'posts': posts})

def struktura(request):
    return render(request,"pews/struktura.html")


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, created_date__month=month, created_date__year=year,  created_date__day=day)
    return render(request,'pews/detail.html', {'post' : post})

def zak(request):
    newslists = NewsList.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "pews/zak.html", {'newslists': newslists})

def post_details(request, year, month, day, newslist):
    newslist = get_object_or_404(NewsList, slug=newslist, created_date__month=month, created_date__year=year, created_date__day=day)
    return render(request,'pews/detailzak.html', {'newslist': newslist})