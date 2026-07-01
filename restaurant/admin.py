from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Restaurant, SocialLink, Profile, ContactRequest


# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    summernote_fields = ('content','address',)

admin.site.register(SocialLink)

admin.site.register(Profile)

@admin.register(ContactRequest)
class ContactUsAdmin(SummernoteModelAdmin):
    list_display = ('__str__',)
    list_filter = ('request_type','reservation_for')
    search_fields = ('request_type','name','email','phone')
    summernote_fields = ('message',)
