from django.test import TestCase
from django.urls import reverse
from .models import Restaurant
from datetime import time

class RestaurantTest(TestCase):

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