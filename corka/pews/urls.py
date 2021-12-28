from django.urls import re_path
from .views import position_list, post_list, about, gal, howtous, test, doc, news, struktura, post_detail, zak, post_details
from django.conf.urls import include, static
from django.conf import settings


urlpatterns = [
    re_path('', post_list, name='post_list'),
    re_path('redux', position_list, name='position_list'),
    re_path('about', about, name='about'),
    re_path('gal', gal, name='gal'),
    re_path('howtous', howtous, name='howtous'),
    re_path('test', test, name='test'),
    re_path('doc', doc, name='doc'),
    re_path('news', news, name='news'),
    re_path('struktura', struktura, name='struktura'),
    re_path('<int:year>/<int:month>/<int:day>/<slug:post>/',
            post_detail, name='post_detail'),
    re_path('zak', zak, name='zak'),


]
