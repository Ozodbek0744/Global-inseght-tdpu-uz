from django.contrib import admin
from .models import News
# Register your models here.


admin.site.register(News)


class NewsAdmin(admin.ModelAdmin):
    list_display = "__all__"


