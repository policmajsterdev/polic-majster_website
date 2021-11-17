from django.db import models

class Gracze(models.Model):

    nazwa = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)


