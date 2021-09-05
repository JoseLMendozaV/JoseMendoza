from django.urls import path
from django.urls.resolvers import URLPattern
from JoseMendoza import views

app_name = 'JoseMendoza'

urlpatterns = [
    path('', views.index, name='index'),
]