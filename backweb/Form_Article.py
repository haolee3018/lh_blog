
from django import forms


class Form_AddArticle(forms.Form):
    title = forms.CharField(min_length=3, required=True,
                            error_messages={
                                'required': '文章标题不能为空',
                                'min_length': '标题长度不能少于5个字符'
                            })
    desc = forms.CharField(min_length=2, required=True,
                           error_messages={
                               'required': '文章描述不能为空',
                               'min_length': '文章描述不能少于2个字符'
                           })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容不能为空'
                              })
    icon = forms.ImageField(required=False)

class EditArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required' : '文章标题是必须填写的',
                                'min_length' : '文章标题不能少于5个字符'
                            })
    desc = forms.CharField(min_length=2, required=True,
                           error_messages={
                               'required': '文章描述不能为空',
                               'min_length': '文章描述不能少于5个字符'
                           })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容是必须填写'
                              })
    icon = forms.ImageField(required=False)