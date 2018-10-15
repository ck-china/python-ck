from django.shortcuts import render,reverse
from django.shortcuts import redirect
from userapp.models import *
from userapp.forms import *
import random
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def login(request):
    #不允许重复登录
    # message='666666666666'
    if request.session.get('is_login',None):
        return redirect(reverse('blog:index1',args=(1,)))
    login_form = UserForm(request.POST)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        message = '所有字段都必须填写'
        if username and password:#确保用户名和密码都不为空
            #通过strip()方法,将用户前后无效的空格去除;
            username = username.strip()
            try:
                user = userlogin.objects.get(name=username)
                if user.password == password:
                    if user.isActiave == True:
                        request.session['is_login'] = True
                        #存了用户名
                        request.session['user_name'] = user.name
                        #存了用户id
                        request.session['user_id'] = user.id
                        return redirect(reverse('blog:index1',args=(1,)))
                    else:
                        message = '用户未激活,请邮箱激活'
                else:
                    message = '密码不正确'
            except:
                message = '用户名不存在'

        return render(request,'login.html',locals())
    else:
        login_form = UserForm()
        return render(request,'login.html',locals())


def logout(request):
    if not request.session.get('is_login',None):
        return redirect(reverse('blog:index1',args=(1,)))
    request.session.flush()

    return redirect(reverse('blog:index1',args=(1,)))
def suiji():
    a = random.randint(100,200)
    return a
def register(request):
    return render(request,'register.html')
def register1(request):
    u=request.POST.get('username')
    pwd=request.POST.get("password")
    pwd2=request.POST.get("password1")
    mail=request.POST.get("email")
    if u and pwd and pwd2 and mail:
        if pwd == pwd2:
            user_list=userlogin.objects.all()
            name_list=[]
            mail_list=[]
            for i in user_list:
                name_list.append(i.name)
                mail_list.append(i.email)
            if u in name_list:
                mag = "用户已存在"
                return render(request,'register.html',locals())
            elif mail in mail_list:
                mag = '邮箱已被注册'
                return render(request, 'register.html', locals())
            else:
                lizi = userlogin()
                lizi.name = u
                lizi.password = pwd
                lizi.email = mail
                lizi.yanzheng_code = suiji()
                lizi.save()
                msg = '<a href="http://127.0.0.1:8000/user/zuce/{}/{}/">邮箱激活</a>'.format(lizi.name, lizi.yanzheng_code)
                send_mail('注册激活', '', settings.EMAIL_FROM, ['m17634040811@163.com'], html_message=msg)
                return HttpResponse('验证码已发送至邮箱，请前往验证')
        else:
            mag = '俩次密码不一致'
            return render(request, 'register.html', locals())
    else:
        mag = '有空值'
        return render(request, 'register.html', locals())

    #         for i in user_list:
    #             print(i.name,u,'+++++++++++++++++++++++')
    #             if i.name == u:
    #                 mag="用户已存在"
    #                 return render(request,'register.html',locals())
    #             elif i.email == mail:

    #             else:

    #     else:

    # else:

def zuce(request,u,c):
    a = userlogin.objects.get(name=u)
    if a.yanzheng_code == c:
        a.isActiave = True
        a.save()
    return redirect(reverse('user:login'))