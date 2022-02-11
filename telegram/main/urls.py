from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('buy/', views.buy, name = "buy"),
    path('booking/', views.booking, name = "booking"),
    path('resume/', views.resume, name = "resume"), 
]
