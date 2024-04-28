from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index.html'),
    path('about.html/',views.about,name='about.html')
    
    
]
