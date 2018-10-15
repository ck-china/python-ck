from django import forms

from captcha.fields import CaptchaField


class UserForm(forms.Form):
    #label参数用于设置<label>标签
    #max_length  限制字段输出的最大长度.他起到两个作用
    #一是在浏览器页面限制用户输入不可超过字符数,
    #二是在后端服务器验证用户输入的长度也不可超过
    username = forms.CharField(label='用户名',max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label='验证码')