from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.capacity} seats)"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='reservations')
    table = models.ForeignKey(Table,blank=True, null=True, on_delete=models.SET_NULL, related_name='reservations')

    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    party_size = models.PositiveIntegerField()
    reservation_for = models.DateTimeField()

    def __str__(self):
        return f"{self.contact_name} - {self.reservation_date}"