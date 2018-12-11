from django.conf.urls import url
from django.contrib import admin

from web import views

urlpatterns = [
    # 博客首页
    # 127.0.0.1:8090/web/index/
    url(r'^index/', views.index),
]