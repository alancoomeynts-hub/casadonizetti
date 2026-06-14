from django.shortcuts import get_object_or_404, render
from .models import Menu, MenuSection, MenuItem
# Create your views here.
def menu_view(request):
    menu=get_object_or_404(Menu, is_active=True)
    featured_items=MenuItem.objects.filter(is_featured=True)
    return render(request,'menu/menu.html',{'menu':menu,'featured_items':featured_items})


