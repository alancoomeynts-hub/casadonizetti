from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_view, name='reserve'),
    path('cancel/<int:pk>/', views.cancel_reservation, name='cancel_reservation')
]