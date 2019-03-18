from django.db import models
from django.shortcuts import reverse

class Post (models.Model):
    category=models.ManyToManyField('Cate', related_name='pos')
    body = models.TextField()

    def __str__(self):
        return self.body


class Cate (models.Model):
    category = models.TextField()

    def __str__ (self):
        return self.category

    def get_absolute_url(self):
        return reverse('cate_detail_url', kwargs={'category': self.category})