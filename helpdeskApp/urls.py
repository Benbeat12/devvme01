from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('get_help/', views.get_help, name='get_help'),
    path('alldevice/', views.alldevice, name='alldevice'),
    path('reportdevice/', views.reportDevice, name='reportdevice'),
]