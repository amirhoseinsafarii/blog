from django.db import models
from django.core.cache import cache
# Create your models here.


class Post(models.Model):
    """
    Represents a single blog post
    """
    title = models.CharField(max_length=100, verbose_name='عنوان پست')
    created_on = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    body = models.TextField(max_length=500, verbose_name='متن', null=True)
    creator = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='عکس', blank=True, null=True)
    like = models.IntegerField(default=0)
    categories = models.ManyToManyField('blog.Category')

    class Meta:
        ordering = ('title',)
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    """
    Categories for posts

    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=20, unique=True, null=True, blank=False)

    class Meta:
        permissions = []
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name
