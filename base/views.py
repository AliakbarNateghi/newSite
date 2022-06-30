import symbol
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import pro, Order, OrderItem
from .custom import Cart, update_total
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test


def index_view(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'message': None})

    return HttpResponseRedirect(reverse_lazy('pro'))


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
    context_object_name = 'pros'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['pros'] = context['pros'].filter(user=self.request.user)
        return context


class aboutus(LoginRequiredMixin, ListView):
    template_name = 'aboutus.html'
    model = pro


class cart(LoginRequiredMixin, ListView):
    template_name = 'cart.html'
    model = pro
    success_url = reverse_lazy('pro')


@login_required(redirect_field_name='index')
def additem(request):
    """
    Add orders to cart.
    """
    if request.method == 'POST':
        customer = request.user
        name = request.POST['name']
        kind = request.POST['kind']
        qty = int(request.POST['qty'])
        price = int(request.POST['price'])
        order = Cart(customer)

        for i in range(qty):
            newitem = OrderItem(
                name=name,
                kind=kind,
                price=price,
                order=order)
            newitem.save()
            update_total(order)

    return HttpResponseRedirect(reverse_lazy('pro'))

