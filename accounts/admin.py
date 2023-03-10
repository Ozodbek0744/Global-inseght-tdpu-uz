from django.contrib import admin
from .models import Account

# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'username', 'famly', 'otchestvo', 'image', 'is_admin', 'is_active', 'is_staff']

