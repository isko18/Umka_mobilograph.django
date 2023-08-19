from django.urls import path 
from .views import contacts

urlpatterns = [
    path('contact/', contacts, name="contact")
]