from django.urls import path
from .views import ProList, aboutus

urlpatterns = [
    path('', ProList.as_view(), name='pro'),
    path('aboutus/', aboutus.as_view(), name='aboutus')
]
