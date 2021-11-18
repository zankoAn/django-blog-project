from django.contrib import admin
from post.models import Post, Comment
from django.utils.translation import gettext_lazy as _


@admin.register(Post)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "publish_date", "status")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "status")
    list_editable = ("status",)
    list_display_links = ("title",)
    
@admin.register(Comment)
class Data(admin.ModelAdmin):
    pass
