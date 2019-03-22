from django.db import models
from django.shortcuts import reverse

class Post (models.Model):
    category=models.ForeignKey('Cate', on_delete=models.CASCADE, related_name='pos',default =None)
    body = models.TextField()

    def __str__(self):
        return self.body


class Cate (models.Model):
    category = models.TextField()

    def __str__ (self):
        return self.category

    def get_absolute_url(self):
        return reverse('cate_detail_url', kwargs={'pk': self.id})
    
    def get_create_url(self):
        return reverse('post_create_detail_url', kwargs={'pk': self.id})

    