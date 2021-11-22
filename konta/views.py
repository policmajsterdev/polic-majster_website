from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests

def woc():

    url = 'https://api.whatsonchain.com/v1/bsv/main/chain/info'
    response = requests.get(url)
    data_all = response.json()
    headers = data_all['headers']
    return headers


def home(request):

    return render(request, 'konta/dash.html')


def wpis(request, my_id):
    data_all = woc()
    strona = BlogPost.objects.get(id=my_id)
    context = {'strona': strona, 'data_all': data_all}
    return render(request, 'konta/wpis.html', context)


def archiwum(request):
    posty = BlogPost.objects.all()
    total_posts = posty.count()
    context = {'posty': posty, 'total_posts': total_posts}
    return render(request, 'konta/archiwum.html', context)


