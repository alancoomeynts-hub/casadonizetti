from datetime import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .forms import ReservationForm
from .models import Reservation, Table

User=get_user_model()

class ReservationViewTests(TestCase):
    """
    Test suite for reservation-related views.

    Covers in order: rendering the reservation form, handling
    reservation submissions, managing table availability, canceling reservations and editing reservations.
    """
    def setUp(self):
        self.user=User.objects.create_user(username='testuser',email='test@test.com',password='password123')

        self.table_1=Table.objects.create(name='Test Table 1',capacity=5, is_available=True)
        self.table_2=Table.objects.create(name='Test Table 2',capacity=3, is_available=True)

    def test_render_reservation_form(self):
        self.client.login(username='testuser',password='password123')
        response=self.client.get(reverse('reserve'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ReservationForm)

    def test_reservation_view_successful_submission(self):
        self.client.login(username='testuser',password='password123')

        post_data={
            'party_size':3,
            'reservation_date':'2026-06-30',
            'reservation_time':'19:00',
        }

        response = self.client.post(reverse('reserve'), post_data)

        self.assertEqual(response.status_code, 302)

        reservation=Reservation.objects.first()
        self.assertEqual(reservation.user, self.user)
        self.assertEqual(reservation.contact_name, 'testuser')
        self.assertEqual(reservation.contact_email, 'test@test.com')

        self.assertEqual(reservation.table, self.table_2)

    def test_reservation_view_table_unavailable(self):
        self.client.login(username='testuser',password='password123')

        Reservation.objects.create(user=self.user,
                                   table=self.table_1,
                                   party_size=5,
                                   reservation_for=datetime(2026, 6, 30, 19, 0),
                                   contact_name='testuser',
                                   contact_email="test@test.com"
                                   )
        Reservation.objects.create(user=self.user,
                                   table=self.table_2,
                                   party_size=3,
                                   reservation_for=datetime(2026, 6, 30, 19, 0),
                                   contact_name='testuser',
                                   contact_email="test@test.com"
                                   )
        post_data={
            'party_size': 2,
            'reservation_date': '2026-06-30',
            'reservation_time': '19:00',
        }

        response = self.client.post(reverse('reserve'), post_data)

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], None, 'Sorry, no tables are available at that time or party size.')

    def test_cancel_reservation(self):
        self.client.login(username='testuser',password='password123')

        reservation = Reservation.objects.create(user=self.user,
                                   table=self.table_1,
                                   party_size=5,
                                   reservation_for=datetime(2026, 6, 30, 19, 0),
                                   contact_name='testuser',
                                   contact_email="test@test.com"
                                   )

        self.assertEqual(Reservation.objects.count(), 1)
        response=self.client.post(reverse('cancel_reservation',args=[reservation.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 0)

    def test_edit_reservation(self):
        self.client.login(username='testuser',password='password123')

        reservation = Reservation.objects.create(user=self.user,
                                   table=self.table_1,
                                   party_size=5,
                                   reservation_for=datetime(2026, 6, 30, 19, 0),
                                   contact_name='testuser',
                                   contact_email="test@test.com"
                                   )
        post_data={
            'party_size': 3,
            'reservation_date': '2026-07-01',
            'reservation_time': '20:00',
        }

        response = self.client.post(reverse('edit_reservation', args=[reservation.pk]),post_data)

        self.assertEqual(response.status_code, 302)
        reservation.refresh_from_db()
        self.assertEqual(reservation.party_size, 3)