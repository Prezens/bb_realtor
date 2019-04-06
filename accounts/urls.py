from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login_url'),
    path('register/', register_view, name='register_url'),
    path('logout/', logout_view, name='logout_url'),
    path('dashboard/', dashboard_view, name='dashboard_url'),
]

