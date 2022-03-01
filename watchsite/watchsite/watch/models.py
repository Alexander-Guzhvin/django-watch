from django.db import models
from django.urls import reverse



class Watch(models.Model):
    photo = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.SlugField(max_length=40, unique=True, db_index=True, verbose_name="URL")
    price = models.TextField(blank=True)
    content = models.TextField(blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=40, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})