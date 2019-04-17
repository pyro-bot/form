from betterforms.multiform import MultiModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import formset_factory, modelformset_factory
from collections import OrderedDict

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
Dformm = modelformset_factory(Essence, Dform, extra = 3, max_num = 20,can_delete=True)

        
class Myform2(MultiModelForm):
    form_classes = {
        'post': myform,
        'dform': Dformm,
    }
        
    def save(self, commit=True):
        # objects = OrderedDict(
        #     (key, form.save(commit))
        #     for key, form in self.forms.items()
        # )
        objects = {}
        objects['post'] = self.forms['post'].save(commit)

        self.forms['dform'][0].instance.key = objects['post']
        objects['dform'] = self.forms['dform'].save(commit)


        if any(hasattr(form, 'save_m2m') for form in self.forms.values()):
            def save_m2m():
                for form in self.forms.values():
                    if hasattr(form, 'save_m2m'):
                        form.save_m2m()
            self.save_m2m = save_m2m

        return objects