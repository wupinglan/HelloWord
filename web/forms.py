#coding:utf-8 

from django import forms

class UserForm(forms.Form):
    fileName = forms.CharField(max_length = 30)
    uploadFile = forms.FileField()

class LoginForm(forms.Form):
    # 如果为空则报错
    name = forms.CharField(required=True,error_messages={'required': "用户名不能为空"})
    # # 同时也可以设定长度限制min_length、max_length
    password = forms.CharField(required=True, min_length=5,error_messages={'required': "密码不能为空"})