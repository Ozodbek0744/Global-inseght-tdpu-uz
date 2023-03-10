from uuid import uuid4
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
import random as r
# Create your models here.


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'news/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    @property
    def image_url(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


@receiver(pre_save, sender=News)
def pre_save_news_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
       instance.slug = slugify((str(r.randint(1, 10000))+'-'+str(r.randint(1, 1000))))


@receiver(post_delete, sender=News)
def post_delete_news_receiver(sender, instance, *args, **kwargs):
    instance.image.delete()


