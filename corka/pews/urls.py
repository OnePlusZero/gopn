from django.urls import path
from .views import position_list, post_list, about, gal, howtous, test, doc, news, struktura, post_detail
from django.conf.urls import include, url


urlpatterns = [
    path('', post_list, name='post_list' ),
    path('redux',position_list, name='position_list'),
    path('about',about, name='about'),
    path('gal',gal, name='gal'),
    path('howtous',howtous, name='howtous'),
    path('test',test, name='test' ),
    path('doc',doc, name='doc'),
    path('news',news, name='news'),
    path('struktura',struktura, name='struktura'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail')

]
