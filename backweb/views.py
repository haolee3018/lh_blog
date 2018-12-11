from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.models import MyBlogUser, Article
from backweb.Form_Article import Form_AddArticle


def index(request):
    if request.method == 'GET':
        return render(request, 'backweb/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = MyBlogUser.objects.filter(username=username).first()

        if user:
            err_name = '该账号已被注册，请重新输入'
            return render(request, 'backweb/register.html', {'err_name': err_name})

        if username and password and password2:
            if password != password2:
                err_pwd = '密码不一致，请重新输入密码'
                err_date = {
                    'err_pwd': err_pwd
                }
                return render(request, 'backweb/register.html', err_date)
            else:
                user = MyBlogUser()
                user.username = username
                user.password = password
                user.save()
                return HttpResponseRedirect('/backweb/login/')
        else:
            err_pwd = '账号或密码不能为空！'
            return render(request, 'backweb/register.html', {'err_pwd': err_pwd})


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = MyBlogUser.objects.filter(username=username,
                                             password=password).first()
            if not user:
                err = '用户名或密码错误'
                return render(request, 'backweb/login.html', {'err':err})
            request.session['user_id'] = user.id
            res = HttpResponseRedirect('/backweb/article/')
            return res
        else:
            err = '用户名或密码不能为空'
            return render(request, 'backweb/login.html', {'err': err})


def logout(request):
    # 退出
    # 1. 删除cookie中的sessionid值
    # 2. 或者删除django_session表中的数据
    # 两边都删除
    # request.session.flush()

    # 删除django_session表中的数据
    # request.session.delete(request.session.session_key)

    # 删除session_data中的登陆成功设置的键值对
    del request.session['user_id']

    return HttpResponseRedirect('/backweb/login/')

def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page',1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 7)
        page = paginator.page(page)
        return render(request, 'backweb/article.html', {'page':page})

def add_article(request):
    if request.method == 'GET':
        return render(request, 'backweb/add_article.html')
    if request.method == 'POST':
        form = Form_AddArticle(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title,
                                   desc=desc,
                                   content=content,
                                   icon=icon)
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            return render(request, 'backweb/add_article.html', {'form': form})

def edit_article(request):
    if request.method == 'GET':
        return render(request, 'backweb/edit_article.html')


