from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
from bookings import forms


# Create your models here.
class Restaurant(models.Model):
    """Represent a restaurant's core contact and opening details."""

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
    """Represent a social media link for a restaurant."""

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='social_links')
    platform=models.CharField(max_length=20)
    url = models.URLField()
    icon = models.CharField(max_length=50,default='')

    def __str__(self):
        return f'{self.platform}'


class Profile(models.Model):
    """Represent additional contact details for a user profile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class ContactRequest(models.Model):
    """Store messages sent to the restaurant's contact form."""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='contact_us')
    request_type = models.CharField(max_length=20,
                                    default='inquiry',
                                    choices=(
                                        ('private_dining', 'Private Dining Reservation'),
                                        ('inquiry', 'Inquiry'),

                                    ))
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    party_size = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(50)])
    reservation_for = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.request_type=='private_dining':
            if not self.reservation_for:
                raise ValidationError({'reservation_for' : 'Please enter the date for private dining reservation.'})
        else:
            self.party_size=None
            self.reservation_for=None

    def __str__(self):
        return f'{self.name} - {self.get_request_type_display()}'