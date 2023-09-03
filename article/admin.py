from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", ]
    list_display_links = ["title"]
    search_fields = ["title", "content", "created_at"]
    list_filter = ["title"]
