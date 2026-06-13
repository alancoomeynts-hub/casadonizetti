from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class MenuSection(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)
    featured_image=CloudinaryField('image',blank=True,null=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.name