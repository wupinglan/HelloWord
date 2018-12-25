#code = utf-8
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from web.models import Student
from web.models import User
from web.forms import UserForm,LoginForm
from web.models import File
import json
# 登录校验
def Login(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST, request.FILES)
        if loginform.is_valid():
            user_name = request.POST.get("name","")
            user_password = request.POST.get("password","")
            is_name_exist=User.objects.filter(name = user_name).exists()
            is_password_exist=User.objects.filter(password = user_password).exists()
            if is_name_exist or is_password_exist:
                return render_to_response('uploadOK.html')
            else:
                return render_to_response('login.html',{'error_msg':'用户名或密码错误'})
        else:
            return render_to_response(getFormTips(loginform)) 
    else:
        loginform = LoginForm(initial ={'name': 'sunshore'})
        return render_to_response('login.html')
#插入数据库
def uploads(request):
    if request.method == 'POST':
        userform = UserForm(request.POST, request.FILES)
        # print(userform)
        if userform.is_valid():
            fileinstall = File()
            fileinstall.fileName = userform.cleaned_data['fileName']
            fileinstall.uploadFile = userform.cleaned_data['uploadFile']
            fileinstall.save()
            return render_to_response('uploadOK.html')
    else:
        userform = UserForm(initial ={'fileName': 'sunshore'})
    return render_to_response('upload.html', {'userform': userform})

def Login_install(request):
        return render_to_response('login_install.html',{'error_msg':'用户名或密码错误'})
