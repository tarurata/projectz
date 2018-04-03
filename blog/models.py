from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=25)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    thumbnail = models.ImageField('サムネイル', upload_to='images/', null='True', blank='True')


    def __str__(self):
        return self.title

    def shortentext(self):
        if len(self.text) > 20:
            return self.text[:20] + '...'
        else:
            return self.text


class Comment(models.Model):
    name = models.CharField('お名前', max_length=30, default='名前')
    text = models.TextField('本文')
    post = models.ForeignKey(Post, verbose_name='紐づく記事', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]


class Image(models.Model):
    post = models.ForeignKey(
        Post, verbose_name='紐づく記事', on_delete=models.PROTECT
    )
    src = models.ImageField('画像', upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        """imgタグを生成する。これをそのまま記事欄に貼り付ける。"""
        return "<img src='"+self.src.url+"'>"
        # return '間接リンク:[filter imgpk]{0}[end] 直接リンク:[filter img]{1}[end]'.format(self.pk, self.src.url)
