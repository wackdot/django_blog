from django.contrib import admin

# Register your models here.
from .models import Post

# Connects the Post model with the Admin
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "last_updated", "timestamp"]
    list_display_links = ["title", "last_updated", "timestamp"]
    list_filter = ["last_updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
