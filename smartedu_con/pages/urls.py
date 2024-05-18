from django.urls import path
from . import views
from pages.views import AboutView,IndexView,ContactView

urlpatterns = [
    path('', IndexView.as_view(),name='index.html'),
    path('about.html/',AboutView.as_view(),name='about.html'),
    path('contact.html/',ContactView.as_view(),name='contact'),
    
    
    
]
