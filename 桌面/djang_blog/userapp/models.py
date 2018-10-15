from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class BlogUser(AbstractUser):
    nick_name=models.CharField(verbose_name="昵称",default='',max_length=128)

class EmailVerifyRecord(models.Model):
    code=models.CharField(verbose_name="验证码",max_length=50,default='')
    email=models.EmailField(max_length=50,verbose_name="邮箱")
    send_type=models.CharField(verbose_name="验证码类型",choices=(("register","注册"),("forget","找回密码"),("update_email","更新邮箱")),max_length=30)
    send_time=models.DateTimeField(verbose_name="发送时间",auto_now_add=True)
    class Meta:
        verbose_name='邮箱验证码'
        verbose_name_plural=verbose_name
    def __str__(self):
        return "邮箱是:{},验证码是:{}".format(self.email,self.code)

class userlogin(models.Model):
    gender = (
        ('male','男'),
        ('female','女')
    )
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email =models.EmailField()
    sex = models.CharField(max_length=6,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    yanzheng_code = models.CharField(max_length=200, default=None)
    isActiave = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = verbose_name