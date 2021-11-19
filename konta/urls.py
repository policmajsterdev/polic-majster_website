from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('kontakt/<int:my_id>/', views.kontakt, name="kontakt"),
    path('omnie/', views.omnie, name="omnie"),
]