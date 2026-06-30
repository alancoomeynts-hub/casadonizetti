from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Table(models.Model):
    """
    Represents a reservable table in the restaurant.
    """
    name = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.capacity} seats)"

class Reservation(models.Model):
    """Store a user's table reservation and contact details.

    Reservations include the requested party size and the date and time of the booking.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='reservations')
    table = models.ForeignKey(Table,blank=True, null=True, on_delete=models.SET_NULL, related_name='reservations')

    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    party_size = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    reservation_for = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact_name} - {self.reservation_for}"