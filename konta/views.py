from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):

    return render(request, 'konta/dash.html')


def kontakt(request, my_id):
    strona = BlogPost.objects.get(id=my_id)
    context = {'strona': strona}
    return render(request, 'konta/kontakt.html', context)


def omnie(request):
    posty = BlogPost.objects.all()
    total_posts = posty.count()
    context = {'posty': posty, 'total_posts': total_posts}
    return render(request, 'konta/omnie.html', context)
