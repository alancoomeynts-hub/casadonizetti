from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):
    """
    Unit test class for validating the behavior of the ReservationForm.

    """

    def test_form_valid(self):
        form = ReservationForm(data={
            'party_size': 4,
            'reservation_date': '2026-06-30',
            'reservation_time': '19:00',
        })

        self.assertTrue(form.is_valid(), msg='Form is valid')

    def test_form_invalid(self):
        form = ReservationForm(data={
            'party_size': 0,
            'reservation_date': '',
            'reservation_time': '',
        })
        self.assertFalse(form.is_valid(), msg='Form is invalid')