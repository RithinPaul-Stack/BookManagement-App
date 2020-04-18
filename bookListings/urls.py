from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listings', views.listings, name='listings'),
    path('listings/<int:listing_id>', views.listing, name='listings'),
    path('borrow', views.borrow, name='borrow')
]