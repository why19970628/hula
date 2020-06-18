from django.db import models

# Create your models here.


class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(verbose_name='分类', max_length=32)


class Article(models.Model):
    """
    文章表
    """
    status_choices = (
        (1, '发布'),
        (2, '删除')
    )
    title = models.CharField(verbose_name='分类', max_length=32)
    summary = models.CharField(verbose_name='简介', max_length=225)
    content = models.TextField(verbose_name='文章内容')
    category = models.ForeignKey(verbose_name='分类', to='Category', on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name='状态', choices=status_choices, default=1)
