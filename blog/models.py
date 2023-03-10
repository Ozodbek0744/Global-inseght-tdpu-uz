from django.db import models

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
import random as r
from django.utils.text import slugify
from django.conf import settings


class BlogVideo(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    url = models.URLField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

    # @property
    # def blog_author_image(self):
    #     return self.author.username


@receiver(pre_save, sender=BlogVideo)
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify((str(r.randint(1, 10000))+"-"+str(r.randint(1, 10000))))
        

