from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import Course
from . forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from teachers.models import Teacher

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available= True).order_by('-date')[:2]
        context['total_course'] = Course.objects.filter(available=True).count()
        context['total_students'] = User.objects.count()
        context['total_teachers'] = Teacher.objects.count()
        return context


class AboutView(TemplateView):
    template_name='about.html'

#def about(request):
 #   return render(request,'about.html')

class ContactView(SuccessMessageMixin,FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = "Mesajı başarılı olarak gönderdik"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
