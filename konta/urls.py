from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('wpis/<int:my_id>/', views.wpis, name="wpis"),
    path('archiwum/', views.archiwum, name="archiwum"),
    path('komentarze/', views.odprawa, name="komentarze"),
    path('dodaj_komentarz/', views.dodaj_komentarz, name="dodaj_komentarz"),
    path('ogrze/', views.ogrze, name="ogrze"),
    path('kontakt/', views.kontakt, name="kontakt"),
    path('python/', views.python, name="python"),
]