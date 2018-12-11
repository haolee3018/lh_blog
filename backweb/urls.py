from django.conf.urls import url

from backweb import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^article/', views.article, name='article'),
    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^edit_article/', views.edit_article, name='edit_article'),

]