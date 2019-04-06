from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('about/', about_view, name='about_url')
]

