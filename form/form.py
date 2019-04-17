from betterforms.multiform import MultiModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import formset_factory, modelformset_factory

from .models import Post, Essence, TypeEssence

class myform (forms.ModelForm):
    class Meta:
        model=Post
        fields=['body']
        widgets={
            'body':forms.TextInput(attrs={'size':150,'title':'Запрос'})
        }
        labels={
            'body': _('Запрос')
        }

class Dform (forms.ModelForm):
    class Meta:
        model = Essence
        fields = ['position', 'text', 'essence_cat']
        widgets = {
            'position':forms.TextInput(attrs={'class':'pos' ,'size':5,'title':'Позиция'}),
            'text':forms.TextInput(attrs={'class':'text','size':50,'title':'Сущность'}),
            
        }
        labels={
            'position': _('Позиция'),
            'text': _('Сущность'),
            'essence': _('Категория сущности'),
        }
Dformm = formset_factory(Dform, extra = 3, max_num = 20,can_delete=True)

        
class Myform2(MultiModelForm):
    form_classes = {
        'post': myform,
        'dform': Dformm,
    }
        
