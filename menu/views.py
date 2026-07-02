from django.shortcuts import get_object_or_404, render
from .models import Menu, MenuSection, MenuItem
# Create your views here.
def menu_view(request):
    """
    Display the active :model:`menu.Menu` and featured
    :model:`menu.MenuItem` instances..

    **Context**

    ``menu``
        The active instance of :model:`menu.Menu`.

    ``featured_items``
        A queryset of featured :model:`menu.MenuItem` instances.

    **Template:**

    :template:`menu/menu.html`
    """
    menu=get_object_or_404(Menu, is_active=True)
    featured_items=MenuItem.objects.filter(is_featured=True)
    return render(request,
    'menu/menu.html',
         {'menu':menu,'featured_items':featured_items}
                  )


