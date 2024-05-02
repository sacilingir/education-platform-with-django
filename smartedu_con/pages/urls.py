from django.urls import path
from . import views
from pages.views import AboutView,IndexView

urlpatterns = [
    path('', IndexView.as_view(),name='index.html'),
    path('about.html/',AboutView.as_view(),name='about.html'),
    
    
    
]
