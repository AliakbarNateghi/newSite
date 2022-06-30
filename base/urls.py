from django.urls import path
from .views import ProList, aboutus, cart, CustomLoginView, RegisterPage, index_view, additem
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('pro/', ProList.as_view(), name='pro'),
    path('additem/', additem, name='additem'),
    path('aboutus/', aboutus.as_view(), name='aboutus'),
    path('cart/', cart.as_view(), name='cart')
]
