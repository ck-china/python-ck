from django.shortcuts import render
from userapp.models import BlogUser
from .models import *
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
# def index(request):
#     banner_list=Banner.objects.all()
#     all_post=Post.objects.all().count()
#     post_list=Post.objects.all().order_by("-pub_date")[:10]
#     BlogCategory_list=BlogCategory.objects.all()
#     FriendlyLink_list=FriendlyLink.objects.all()
#
#     conmment_list=Post.objects.filter(commnet__content__isnull=False)
#     new_list=[]
#     for i in conmment_list:
#         if i not in new_list:
#             new_list.append(i)
#     conmment_list=new_list
#     ad_list=ADModel.objects.all()
#     if request.method == "POST":
#         kwd = request.POST.get("keyword")
#         a_list = Post.objects.filter(Q(title__icontains=kwd) | Q(content__icontains=kwd))
#         try:
#             print(a_list[0])
#         except:
#             info = "查找的内容不存在"
#         return render(request,"list.html",locals())
#     return render(request,'index.html',locals())


def index1(request,pIndex):
    banner_list=Banner.objects.all()
    all_post=Post.objects.all().count()
    post_list=Post.objects.all().order_by("-pub_date")
    a_lis=post_list
    BlogCategory_list=BlogCategory.objects.all()
    FriendlyLink_list=FriendlyLink.objects.all()

    conmment_list=Post.objects.filter(commnet__content__isnull=False)
    new_list=[]
    for i in conmment_list:
        if i not in new_list:
            new_list.append(i)
    conmment_list=new_list
    ad_list=ADModel.objects.all()
    if request.method == "POST":
        kwd = request.POST.get("keyword")
        a_list = Post.objects.filter(Q(title__icontains=kwd) | Q(content__icontains=kwd))
        try:
            print(a_list[0])
        except:
            info = "查找的内容不存在"
        return render(request,"list.html",locals())
    p=Paginator(post_list,1)
    if pIndex == '':
        pIndex="1"
    pIndex=int(pIndex)
    post_list=p.page(pIndex)
    plist=p.page_range

    return render(request,'index.html',locals())





def list(request):

    a_list=Post.objects.all()
    conmment_list = Post.objects.filter(commnet__content__isnull=False)
    new_list = []
    for i in conmment_list:
        if i not in new_list:
            new_list.append(i)
    conmment_list = new_list
    ad_list=ADModel.objects.all()
    if request.method == "POST":
        kwd=request.POST.get("keyword")
        a_list=Post.objects.filter(Q(title__icontains=kwd)|Q(content__icontains=kwd))
        try:
            print(a_list[0])
        except:
            info="查找的内容不存在"
    tags=Tage.objects.all()
    new_list=[]
    for i in tags:
        if i not in new_list:
            new_list.append(i)
    tags=new_list
    return render(request,'list.html',locals())





def show(request,bid):
    obj=Post.objects.get(pk=bid)
    tag=obj.tags.all()
    com_list = Post.objects.filter(commnet__content__isnull=False)
    new_lis = []
    for i in com_list:
        if i not in new_lis:
            new_lis.append(i)
        else:
            pass
    com_list = new_lis
    ad_list = ADModel.objects.all()
    a=obj.category_id
    xiangguang=Post.objects.filter(category_id=a)
    new_lis=[]
    for i in xiangguang:
        if i != obj:
            new_lis.append(i)
    xiangguang=new_lis
    all_post=Post.objects.all().count()
    arg_list=obj.commnet_set.all()

    if request.method == "POST":
        kwd=request.POST.get("keyword")
        if kwd:
            a_list = Post.objects.filter(Q(title__icontains=kwd) | Q(content__icontains=kwd))
            try:
                print(a_list[0])
            except:
                info = "查找的内容不存在"
            return render(request, "list.html", locals())

        name=request.POST.get("name")
        mail=request.POST.get("mail")
        content=request.POST.get("comment-textarea")
        if name and content:
            try:
                use=BlogUser.objects.get(nick_name=name)
            except:
                return HttpResponse("该用户不存在")
            con_use=Commnet()
            con_use.post=obj
            con_use.user=use
            con_use.content=content
            con_use.save()
        else:
            return HttpResponse("有空值")
        return HttpResponse("ok")

    return render(request,'show.html',locals())
def list2(request,a):
    a_list = Post.objects.filter(tags__post__category_id=a)
    new_list=[]
    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    a_list=new_list
    conmment_list = Post.objects.filter(commnet__content__isnull=False)
    new_list = []
    for i in conmment_list:
        if i not in new_list:
            new_list.append(i)
    conmment_list = new_list
    ad_list = ADModel.objects.all()
    if request.method == "POST":
        kwd = request.POST.get("keyword")
        a_list = Post.objects.filter(Q(title__icontains=kwd) | Q(content__icontains=kwd))
        try:
            print(a_list[0])
        except:
            info = "查找的内容不存在"
    tags = Tage.objects.all()
    oolist=Post.objects.all()
    for i in oolist:
        print(i.tags,"+++++++++++++++++++++++++++++++++")
    new_list = []

    for i in tags:
        if i not in new_list:
            new_list.append(i)
    tags = new_list
    return render(request, 'list.html', locals())