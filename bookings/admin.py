from django.contrib import admin
from .models import Table, Reservation

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    list_filter = ('is_available','capacity',)
    search_fields = ('name',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('__str__','table','party_size',)
    list_filter = ('reservation_for','table','user')
    search_fields = ('user__username','contact_name','contact_email')

