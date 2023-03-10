from django.db import models
from django.conf import settings

from blog.models import BlogVideo


class Comment(models.Model):
    blog = models.ForeignKey(BlogVideo, related_name="comment", on_delete=models.CASCADE, null=True)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="comment", null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog}-{self.author}"


class Izoh(models.Model):
    comment = models.ForeignKey(Comment, related_name="izoh", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="izoh", on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment}-{self.author}"


