from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ("id", "title", "text")
    list_display = ("id", "title")
    fields = ("id", "author", "title", "text", "created_at", "published_at")
    readonly_fields = ("id", "created_at", "published_at")


admin.site.register(Post, PostAdmin)
