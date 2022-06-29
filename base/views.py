import symbol
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import pro
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pro')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = _name = True
    success_url = reverse_lazy('pro')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pro')
        return super(RegisterPage, self).get(*args, **kwargs)


class ProList(LoginRequiredMixin, ListView):
    model = pro
    context_object_name = 'pro'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pro'] = context['pro'].filter(user=self.request.user)
        return context


class aboutus(LoginRequiredMixin, ListView):
    template_name = 'aboutus.html'
    model = pro


class cart(LoginRequiredMixin, ListView):
    template_name = 'cart.html'
    model = pro
    success_url = reverse_lazy('pro')

# class additem(ListView):
#     model = pro
#     success_url = reverse_lazy('pro')
