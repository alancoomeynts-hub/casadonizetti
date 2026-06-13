from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Menu, MenuSection, MenuItem

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','slug','is_active')
    list_filter = ('is_active',)
    search_fields = ('name','slug',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuSection)
class MenuSectionAdmin(admin.ModelAdmin):
    list_display = ('name','menu','is_active','sort_order','slug')
    list_filter = ('name','is_active',)
    search_fields = ('name','slug','menu__name')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name','section','is_active','sort_order', 'price','is_featured')
    list_filter = ('is_active','is_featured','section','section__menu')
    search_fields = ('name','description','section__name')


