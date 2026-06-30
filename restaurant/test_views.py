from django.test import TestCase
from django.urls import reverse
from .models import Restaurant, Profile
from bookings.forms import ReservationForm
from bookings.models import Reservation, Table
from django.contrib.auth import get_user_model
from datetime import datetime, time


User=get_user_model()

class RestaurantViewsTest(TestCase):

    def test_render_restaurant(self):
        self.restaurant=Restaurant(name="Test Restaurant", slug="test-restaurant",
                                   content="this is a test restaurant",email="test@test.ie",phone="12345678",address="test address",
                                   open_at=time(12, 0), closes_at=time(22, 30),)
        self.restaurant.save()

        response = self.client.get(reverse("homepage"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")
        self.assertEqual(response.context["restaurant"], self.restaurant)

    def test_homepage_returns_404_when_restaurant_missing(self):

        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 404)

class ProfileViewsTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='password123'
        )

        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@test.com',
            password='password123'

        )

        self.user3 = User.objects.create_user(
            username='testuser3',
            email='test3@test.com',
            password='password123'

        )

        self.profile1 = Profile.objects.create(
            user=self.user1,
            phone='07123456789',
            address='1 High Street'
        )

        self.profile2 = Profile.objects.create(
            user=self.user2,
            phone='07999999999',
            address='2 Main Street'
        )

        self.table=Table.objects.create(
            name="Test Table",
            capacity=5,
            is_available=True
        )

    def test_render_profile(self):
        self.client.login(username='testuser',password='password123')
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user1)
        self.assertEqual(response.context['profile'], self.profile1)
        self.assertIsInstance(response.context['form'], ReservationForm)

    def test_profile_renders_404_when_profile_missing(self):
        self.client.login(username='testuser3',password='password123')
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 404)

    def test_profile_renders_logged_in_user_reservations(self):
        reservation1=Reservation.objects.create(
            user=self.user1,
            table=self.table,
            party_size=2,
            reservation_for=datetime(2026, 6, 30, 19, 0),
            contact_name='testuser',
            contact_email='test@test.com'
        )

        reservation2=Reservation.objects.create(
            user=self.user2,
            table=self.table,
            party_size=3,
            reservation_for=datetime(2026, 7, 1, 20, 0),
            contact_name='testuser2',
            contact_email='test2@test.com'
        )

        self.client.login(username='testuser',password='password123')
        response = self.client.get(reverse("profile"))

        reservation_list=response.context['reservations']
        self.assertIn(reservation1, reservation_list)
        self.assertNotIn(reservation2, reservation_list)


