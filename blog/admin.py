from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'published_at')