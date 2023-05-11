from django.contrib import admin
from website.models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(Post, PostAdmin)
