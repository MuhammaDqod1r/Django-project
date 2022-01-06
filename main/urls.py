from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('get_number/', get_number, name='get_number')  
]