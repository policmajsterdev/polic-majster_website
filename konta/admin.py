from django.contrib import admin

from .models import Gracze, BlogPost, Comment

admin.site.register(Gracze)
admin.site.register(BlogPost)
admin.site.register(Comment)
