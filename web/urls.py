from django.urls import path 
from .views import *

app_name = 'web'

urlpatterns = [
    path('',Home,name='home'),
    path('nepal',nepal,name='nepal'),
    path('world',world,name='world'),
]