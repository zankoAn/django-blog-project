from django.contrib import admin
from post.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "thumbnail_preview", "title", "publish_date", "status")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "status")
    list_editable = ("status",)
    list_display_links = ("title",)


@admin.register(Comment)
class Data(admin.ModelAdmin):
    pass
