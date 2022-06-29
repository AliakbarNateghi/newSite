from django.urls import path
from .views import ProList, aboutus, cart, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('', ProList.as_view(), name='pro'),
    path('aboutus/', aboutus.as_view(), name='aboutus'),
    path('cart/', cart.as_view(), name='cart')
]
