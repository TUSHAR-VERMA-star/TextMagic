from django.contrib import admin
from django.urls import path
from . import views
from django.views.static import server
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
