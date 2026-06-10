from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Restaurant, SocialLink

# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    summernote_fields = ('content','address',)

admin.site.register(SocialLink)