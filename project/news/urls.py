from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('create/', createNews, name='create')
]