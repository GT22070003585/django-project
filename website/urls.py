from django.urls import path, include
from . import views

urlpatterns = [
path('shop/', views.index, name='shop'),
path('contact/', views.contact),
path('shipping/', views.shipping),
]
