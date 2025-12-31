from django.urls import path
from . import views

urlpatterns = [
    path('appone/', views.app1)
]