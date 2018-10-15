from django.db import models
from userapp.models import BlogUser
# Create your models here.
class Banner(models.Model):
    title=models.CharField(verbose_name="标题",max_length=50)
    cover=models.ImageField(verbose_name="轮播图",upload_to="static/images/banner")
    link_url=models.URLField("图片链接",max_length=128)
    idx=models.IntegerField(verbose_name="索引")
    is_active=models.BooleanField(verbose_name='是否激活',default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name
class BlogCategory(models.Model):
    name=models.CharField(verbose_name="分类名称",max_length=20,default='')
    class Meta:
        verbose_name="博客分类"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class Tage(models.Model):
    name=models.CharField(verbose_name="标签名称",max_length=20,default='')
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class Post(models.Model):
    user=models.ForeignKey(BlogUser,verbose_name="作者")
    category=models.ForeignKey(BlogCategory,verbose_name='博客分类',default=None)
    tags=models.ManyToManyField(Tage,verbose_name='标签')
    title=models.CharField(verbose_name="标题",max_length=50)
    content=models.TextField(verbose_name='内容')
    pub_date=models.DateTimeField(verbose_name="发布时间",auto_now_add=True)
    cover=models.ImageField(verbose_name='封面',upload_to="static/images/post",default=None)
    views=models.IntegerField(verbose_name='浏览数',default=0)
    recomment=models.BooleanField(verbose_name='推荐博客',default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='博客'
        verbose_name_plural=verbose_name

class Commnet(models.Model):
    post=models.ForeignKey(Post,verbose_name="博客")
    user=models.ForeignKey(BlogUser,verbose_name='用户')
    pub_date=models.DateTimeField(verbose_name='发布时间',auto_now_add=True)
    content=models.TextField(verbose_name='内容')
    def __str__(self):
        return self.content
    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name
class FriendlyLink(models.Model):
    title=models.CharField(verbose_name='标题',max_length=50)
    link=models.CharField(verbose_name='链接',max_length=100,default='')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='友情链接'
        verbose_name_plural= verbose_name

class ADModel(models.Model):
    img=models.ImageField(verbose_name='图片',upload_to='static/images/ad')
    ad_link=models.CharField(verbose_name="广告链接",max_length=128)
    ad_title=models.CharField(verbose_name='广告合作单位',max_length=20)
    ad_views=models.IntegerField(verbose_name='点击量')
