from django.urls import path

from . import views #import from this dir

app_name = "main"

urlpatterns=[
    path('', views.index, name='index'),
    path('requests', views.requests, name='requests') 
]



#token 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