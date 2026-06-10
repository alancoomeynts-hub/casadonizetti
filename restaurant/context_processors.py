from .models import Restaurant, SocialLink

def footer(request):
    restaurants = Restaurant.objects.first()
    social_links = SocialLink.objects.all()

    return {
        'restaurants': restaurants,
        'social_links': social_links
    }
