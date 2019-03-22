from django.shortcuts import render
from django.views.generic.edit import CreateView
from django import forms
from django.views.generic import ListView,DetailView
from django.contrib.messages.views import SuccessMessageMixin


from .models import Post,Cate
from .form import myform


class ListPost(ListView):
    
    template_name='form/allpost.html'
    context_object_name='posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-id')

class ListCate(ListView):
    template_name='form/allcate.html'
    context_object_name='cates'

    def get_queryset(self):
        return Cate.objects.all()

class DetailCate(DetailView):
    model=Cate
    template_name='form/category_detail.html'
    context_object_name='cates'

class ListCreateCate(ListView):
    template_name='form/create_cate.html'
    context_object_name='cates'

    def get_queryset(self):
        return Cate.objects.all()


# def posts_list(request):
#     posts = Post.objects.all().order_by('-id')
#     return render(request,'form/allpost.html',context={'posts':posts})

# def cate_list(request):
#     cates = Cate.objects.all()
#     return render(request,'form/allcate.html',context={'cates':cates})




# def cate_detail(request,id):
#     cates = Cate.objects.get(pk=id)
#     return render(request, 'form/category_detail.html',context={'category':cates,'cate_name':cates.category if not None else ''})

# def cate_create(request):
#     cates = Cate.objects.all()
#     return render(request, 'form/create_cate.html',context={'cates':cates})

# def cate_create_detail(request,id):
#     cates = Cate.objects.get(pk=id)
#     return render(request, 'post_create_form.html',context={'category':cates,'cate_name':cates.category if not None else ''})

class PostCreate(CreateView,SuccessMessageMixin):
    model = Post
    form_class=myform
    context_object_name='cates'
    template_name_suffix='_create_form'
    success_url='/create/'
    pk_url_kwarg='pk'
    success_message = "%(calculated_field)s was created successfully"

    