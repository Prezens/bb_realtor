from django.urls import path
from .views import *

urlpatterns = [
    path('', listings_view, name='listings_url'),
    path('<int:listing_id>', listing_view, name='listing_url'),
    path('search/', search_view, name='search_url')
]

