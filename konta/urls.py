from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('wpis/<int:my_id>/', views.wpis, name="wpis"),
    path('archiwum/', views.archiwum, name="archiwum"),
]