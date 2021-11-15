from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('kontakt/', views.kontakt),
    path('omnie/', views.omnie),
]