from django.urls import path
from .views import *
from django.conf import settings


urlpatterns = [
    path('', post_list, name='post_list'),
    path('redux', position_list, name='position_list'),
    path('about', about, name='about'),
    path('gal', gal, name='gal'),
    path('howtous', howtous, name='howtous'),
    path('test', test, name='test'),
    path('doc', doc, name='doc'),
    path('news', news, name='news'),
    path('struktura', struktura, name='struktura'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
    path('zak', zak, name='zak'),


]
