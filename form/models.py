from django.db import models
from django.shortcuts import reverse

class Post (models.Model):
    podcategory=models.ForeignKey('PodCate', on_delete=models.CASCADE, related_name='pos', default = None)
    body = models.TextField()

    def __str__(self):
        return self.body

class PodCate(models.Model):
    podcategory = models.TextField()
    category = models.ForeignKey('Cate', on_delete=models.CASCADE, related_name='categ', default = None)

    def __str__ (self):
        return self.podcategory

    def get_absolute_url(self):
        return reverse('podcate_detail_url', kwargs={'pk':self.category.id,'pke': self.id})
    
    def get_create_url(self):
        return reverse('post_create_detail_url', kwargs={'pk':self.category.id,'pke': self.id})

class Cate (models.Model):
    category = models.TextField()

    def __str__ (self):
        return self.category

    def get_absolute_url(self):
        return reverse('cate_detail_url', kwargs={'pk': self.id})
    
    def get_create_url(self):
        return reverse('podpost_create_url', kwargs={'pk': self.id})

class Essence (models.Model):
    position = models.TextField()
    text = models.TextField()
    body_post = models.ForeignKey('Post',on_delete=models.CASCADE, related_name='body_post', default = None)
    essence_cat = models.ForeignKey('TypeEssence',on_delete=models.CASCADE, related_name='e_c', default = None)
    
    def __str__(self):
        return self.text

class TypeEssence (models.Model):
    eccence_cat = models.TextField()
    
    def __str__(self):
        return self.eccence_cat