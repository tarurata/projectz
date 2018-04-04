from django.contrib import admin
from .models import Category, Post, Image


class ImageInline(admin.TabularInline):
    """記事内画像のインライン"""
    model = Image
    extra = 3


class PostAdmin(admin.ModelAdmin):
    """記事を、管理画面で画像をインラインで埋め込む"""
    inlines = [ImageInline, ]


# Register your models here.
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Post, PostAdmin)  # インライン
