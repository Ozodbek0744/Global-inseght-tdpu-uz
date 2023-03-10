from django.contrib import admin
from .models import BlogVideo
from comment.admin import CommentInline


@admin.register(BlogVideo)
class BlogVideo(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'url', 'author',  'slug')
    inlines = [CommentInline]



