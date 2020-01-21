# Create your models here.
from django.db import models

# 导入内建的User模型
from django.contrib.auth.models import User
from django.utils import timezone


# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。参数on_delete 用于指定数据删除的方式，避免两个关联表数据不一致
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题
    title = models.CharField(max_length=100)

    # 文章正文
    body = models.TextField()

    created = models.DateTimeField(default=timezone.now())

    # 文章更新时间 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类class Meta用于给model定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # ’-created‘ 表明数据应该以倒叙排列
        ordering = ('-created',)

    def __str__(self):
        return self.title
