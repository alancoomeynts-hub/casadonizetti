from .models import Restaurant, SocialLink

def footer(request):
    restaurant = Restaurant.objects.first()
    social_links = SocialLink.objects.all()

    return {
        'restaurant': restaurant,
        'social_links': social_links
    }
