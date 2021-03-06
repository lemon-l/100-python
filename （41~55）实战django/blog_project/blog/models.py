from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章标题
    title = models.CharField('标题', max_length=70)
    # 文章正文
    body = models.TextField('正文')
    # 文章创建时间
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    # 文章最后一次修改时间
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    # 文章摘要
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    '''
    这是分类与标签，分类与标签的模型我们已经定义在上面。
    我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一
    对多的关联关系。且自 django 2.0 以后，ForeignKey 必须传入一个 on_delete 参数用来指定当关联的
    数据被删除时，被关联的数据的行为，我们这里假定当某个分类被删除时，该分类下全部文章也同时被删除，因此     # 使用 models.CASCADE 参数，意为级联删除。
    而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 
    ManyToManyField，表明这是多对多的关联关系。
    同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    https://docs.djangoproject.com/en/2.2/topics/db/models/#relationships
    '''
    # 分类
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    # 标签
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 作者
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # 自定义get_absolute_url方法
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
