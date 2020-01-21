from django.shortcuts import render, redirect
import markdown
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# 视图函数
def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板对象
    context = {'articles': articles}
    # render函数载入模板，并返回context对象
    return render(request, 'article/list.html', context)
    # article/list.html：模板位置          context：传入模板的对象


# 文章详情
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         # 包含 缩写、表格等常用扩展
                                         'markdown.extensions.extra',
                                         # 语法高亮扩展
                                         'markdown.extensions.codehilite',
                                     ])
    context = {'article': article}
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)

@login_required(login_url='/userprofile/login')
def article_create(request):
    # 判断用户是否提交数据
    if request.method == 'POST':
        # 将提交时数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect('article:article_list')
        else:
            return HttpResponse('表单内容有误，请重新填写')
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html')


def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect('article:article_list')


def article_update(request, id):
   # 获取文章对象
   article = ArticlePost.objects.get(id=id)
   if request.method =="POST":
       article_post_form = ArticlePostForm(data=request.POST)
       if article_post_form.is_valid():
           article.title = request.POST['title']
           article.body = request.POST['body']
           article.save()

           return redirect("article:article_detail", id=id)
       else:
           return HttpResponse("表单内容有误,请重新填写")


   else:
       article_post_form = ArticlePostForm()
       context = { 'article': article, 'article_post_form': article_post_form}
       return render(request, 'article/update.html', context)
