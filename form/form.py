from .models import Post
from django import forms

class myform (forms.ModelForm):
    class Meta:
        model=Post
        fields=['body','category']
        widgets={
            'body':forms.TextInput(attrs={'size':200,'title':'Запрос'})
        }
        
        
