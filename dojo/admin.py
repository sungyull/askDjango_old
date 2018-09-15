# dojo/admin.py

from django.contrib import admin
from .models import Post, GameUser


# Register your models here.
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'ip', 'created_at', 'updated_at']
    list_display_links = ['title']


@admin.register(GameUser)
class GameUserAdmin(admin.ModelAdmin):
    list_display = ['server_name','username']
    list_display_links = ['username']