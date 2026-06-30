from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Menu(models.Model):
    """Represent a restaurant menu."""

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class MenuSection(models.Model):
    """Represent a section within a menu."""

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    sort_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order']
        constraints = [
            models.UniqueConstraint(fields=['menu', 'slug'], name='sections_unique_per_menu'),
        ]

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    """Represent an item within a menu section."""

    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_featured = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)
    featured_image=CloudinaryField('image',blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.name