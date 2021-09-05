from django.contrib import admin
from django.urls import path
from django import urls
from django.urls import include
from JoseMendoza import views

urlpatterns = [
    path('', views.index, name='index'),
    path('JoseMendoza/', include('JoseMendoza.urls')),
    path('admin/', admin.site.urls),
]
