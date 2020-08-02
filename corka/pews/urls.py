from django.urls import path
from .views import position_list, post_list, about, gal, howtous, test, doc, news, struktura
from django.conf.urls import include, url


urlpatterns = [
    path('', post_list, name='post_list' ),
    path('redux',position_list),
    path('about',about),
    path('gal',gal),
    path('howtous',howtous),
    path('test',test),
    path('doc',doc),
    path('news',news),
    path('struktura',struktura)
]
