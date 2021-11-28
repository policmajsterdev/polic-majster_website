from django.shortcuts import render
from .forms import CommentForm
from .models import *


def home(request):

    return render(request, 'konta/dash.html')


def wpis(request, my_id):
    strona = BlogPost.objects.get(id=my_id)
    context = {'strona': strona}
    return render(request, 'konta/wpis.html', context)


def archiwum(request):
    posty = BlogPost.objects.all().order_by('-data_utw')
    total_posts = posty.count()
    context = {'posty': posty, 'total_posts': total_posts}
    return render(request, 'konta/archiwum.html', context)


def ogrze(request):

    return render(request, 'konta/ogrze.html')


def odprawa(request):
    komentarze = Comment.objects.all().order_by('-date_added')
    total_komentarze = komentarze.count()
    context = {'komentarze': komentarze, 'total_komentarze': total_komentarze}
    return render(request, 'konta/komentarze.html', context)


def dodaj_komentarz(request):
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'konta/add_komentarze.html', {
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
