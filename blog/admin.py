from django.contrib import admin

from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ("id", "title", "text", "slug")
    list_display = ("id", "title", "slug")
    fields = ("id", "author", "title", "slug", "text", "created_at", "posted_at")
    readonly_fields = ("id", "slug", "created_at", "posted_at")


admin.site.register(Post, PostAdmin)
