from django.contrib import admin
from .models import Category, Post, Image

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
