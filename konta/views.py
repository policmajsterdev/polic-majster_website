from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'konta/dash.html')

def kontakt(request):
    return render(request, 'konta/kontakt.html')

def omnie(request):
    return render(request, 'konta/omnie.html')



# Create your views here.
