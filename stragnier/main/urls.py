from django.urls import path

from . import views #import from this dir

urlpatterns=[
    path('', views.index, name='index')
]