from django.db import models


# 用户
class MyBlogUser(models.Model):
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'myblog_user'


class Article(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length= 100)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'articles'