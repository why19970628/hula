from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """ 用户表 """
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    token = models.CharField(verbose_name="登录认证码",
                             max_length=64, null=True, blank=True)


class Article(models.Model):
    """ 文章表 """
    category_choices = (
        (1, '咨询'),
        (2, '公司动态'),
        (3, '分享'),
        (4, '答疑'),
        (5, '其他'),
    )
    category = models.IntegerField(verbose_name='分类', choices=category_choices)
    title = models.CharField(verbose_name='标题', max_length=32)
    # /media/upload/....
    image = models.CharField(verbose_name='图片路径', max_length=128)
    summary = models.CharField(verbose_name='简介', max_length=255)

    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    read_count = models.IntegerField(verbose_name='浏览数', default=0)

    author = models.ForeignKey(verbose_name='作者', to='UserInfo', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


class ArticleDetail(models.Model):
    article = models.OneToOneField(verbose_name='文章表', to='Article', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='内容')


class Comment(models.Model):
    """ 评论表 """
    article = models.ForeignKey(verbose_name='文章', to='Article',  on_delete=models.CASCADE)
    content = models.TextField(verbose_name='评论')
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo',  on_delete=models.CASCADE)
    # parent = models.ForeignKey(verbose_name='回复',to='self', null=True,blank=True)
