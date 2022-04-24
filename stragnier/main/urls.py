from django.urls import path

from . import views #import from this dir

urlpatterns=[
    path('', views.index, name='index')
]


#token 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