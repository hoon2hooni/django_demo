from django.contrib import admin
from .models import Post

class PostAdminConfig(admin.ModelAdmin):
    list_filter = ['title']

admin.site.register(Post,PostAdminConfig)
# Register your models here.
