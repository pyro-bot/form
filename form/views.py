from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post,Cate


def posts_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request,'form/allpost.html',context={'posts':posts})

def cate_list(request):
    cates = Cate.objects.all()
    return render(request,'form/allcate.html',context={'cates':cates})

def cate_detail(request,category):
    cates = Cate.objects.get(category__iexact=category)
    return render(request, 'form/category_detail.html',context={'category':cates})

class Post_create(CreateView):
    model = Post
    fields=['category','body']
    template_name_suffix='_create_form'
    success_url='/'