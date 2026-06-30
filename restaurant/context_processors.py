from .models import Restaurant, SocialLink

def footer(request):
    """
    Generates context data for the footer section of the home page.

    """

    restaurant = Restaurant.objects.first()
    social_links = SocialLink.objects.all()

    return {
        'restaurant': restaurant,
        'social_links': social_links
    }
