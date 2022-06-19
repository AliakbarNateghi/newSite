import symbol
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import pro
from django.views.generic.list import ListView


class ProList(ListView):
    model = pro
    context_object_name = 'pros'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_input = self.request.GET.get('')
        context['image'] = image_input
        return context


class aboutus(ListView):
    template_name = 'aboutus.html'
    model = pro
