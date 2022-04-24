from django.urls import path

from . import views #import from this dir

urlpatterns=[
    path('', views.index, name='index'),
    path('<str:url_val>', views.get_url) #take string, and pass tp get_url
]



#token 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