from django.shortcuts import render
from django.views.generic.edit import CreateView
from django import forms
from django.views.generic import ListView,DetailView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _



from .models import Post,Cate,PodCate
from .form import myform, Myform2


class ListPost(ListView):
    template_name='form/allpost.html'
    context_object_name='posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-id')

# отображаю все категории
class ListCate(ListView):
    template_name='form/allcate.html'
    context_object_name='cates'

    def get_queryset(self):
        return Cate.objects.all()

# отображаю все подкатегории категории
class DetailCate(DetailView):
    model = Cate
    template_name='form/podcate_detail.html'
    context_object_name='cates'
    pk_url_kwarg = "pk"

# отображаю все запросы с подкатегорией
class DetailPodCate(DetailView):
    model = PodCate
    template_name='form/podcategory_detail.html'
    context_object_name='cates'
    pk_url_kwarg = "pke"


class PostUpdate(UpdateView):
    model = Post
    template_name_suffix='_update_form'
    fields=['podcategory','body']
    success_url='/'


# отображаю все категории для создания
class ListCreateCate(ListView):
    template_name='form/create_cate.html'
    context_object_name='cates'

    def get_queryset(self):
        return Cate.objects.all()

# отображаю все подкатегории категории для создания
class CreateDetailCate(DetailView):
    model = Cate
    template_name='form/create_podcate_detail.html'
    context_object_name='cates'
    pk_url_kwarg = "pk"



class PostCreate(CreateView):
    model = Post
    form_class=Myform2
    context_object_name='cates'
    template_name_suffix='_create_form'
    success_url='/create/'
    
    
    def form_valid(self, form):
        form['post'].instance.podcategory = PodCate.objects.get(pk=self.kwargs.get('pke'))
        form['dform'].initial = [ {'body_post':form['post'].instance.body}] 
        post = form['post'].save(commit = False)
        dform = form['dform'].save(commit = False)
        dform.post = post
        dform.save()
        

        return super(PostCreate,self).form_valid(form)

    