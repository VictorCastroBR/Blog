from django.contrib import admin
from .models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'created']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'author', 'comment', 'created']


