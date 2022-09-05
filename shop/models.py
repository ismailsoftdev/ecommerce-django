from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
import os


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_lisy_by_category', args=[self.slug])




def save_image(instance, filename):
    upload_to = 'products/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = '{}/{}.{}'.format(instance.category.name, instance.name, ext)
    return os.path.join(upload_to, filename)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=save_image, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])
