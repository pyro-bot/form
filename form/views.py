from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django import forms
from django.views.generic import ListView,DetailView, RedirectView
from django.contrib.messages.views import SuccessMessageMixin


from . import models
from . import form

class Index(RedirectView):
    url = reverse_lazy('form:context-list')


class ContextList(ListView):
    model = models.Context
    template_name = 'form/context-list.html'


class ContextSelect(DetailView):
    model = models.Context
    template_name = 'form/context-select.html'


class ExampleList(DetailView):
    model = models.TrainExample


class NewExample(CreateView):
    model = models.TrainExample


    fields = ['example']
    template_name = 'form/form.html'

    def form_valid(self, form):
        form.instance.intent = models.Intent.objects.get(pk=self.kwargs.get('pk'))
        return super(NewExample, self).form_valid(form)
