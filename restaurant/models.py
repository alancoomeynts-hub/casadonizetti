from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    open_at = models.TimeField(blank=True, null=True)
    closes_at = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class SocialLink(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='social_links')
    platform=models.CharField(max_length=20)
    url = models.URLField()
    icon = models.CharField(max_length=50,default='')

    def __str__(self):
        return f'{self.platform}'