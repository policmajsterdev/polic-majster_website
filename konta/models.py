from django.db import models
from django.contrib.auth.models import User


class Gracze(models.Model):

    nazwa = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nazwa


class BlogPost(models.Model):
    tytul = models.CharField(max_length=150, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tresc = models.TextField()
    data_utw = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.tytul + " | autor: " + str(self.autor)


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.post.tytul, str(self.name))
