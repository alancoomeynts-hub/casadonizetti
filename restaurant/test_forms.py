from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.signup_forms import CustomSignupForm
from django.urls import reverse
from .models import Profile,Restaurant,ContactRequest
from .forms import ContactUsForm

class TestCustomSignupForm(TestCase):

    """
    Unit test class to verify the functionality of the CustomSignupForm.

    This class contains test cases for valid and invalid form data,
    and proper user and profile creation with AllAuth.

    """
    def test_signup_form(self):
        form = CustomSignupForm(data={
            'username': 'johndoe',
            'email': 'john@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'address': '123 Main St',

        })

        self.assertTrue(form.is_valid())

    def test_signup_form_invalid(self):
        form = CustomSignupForm(data={
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
            'first_name': '',
            'last_name': '',
            'phone': '',
            'address': '',
        })
        self.assertFalse(form.is_valid())

    def test_signup_form_user_and_profile_creation(self):

        user=User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='password123')

        form = CustomSignupForm(data={
            'username': 'johndoe',
            'email': 'john@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'address': '123 Main St',

        })

        self.assertTrue(form.is_valid())
        form.signup(request= None ,user=user)

        user.refresh_from_db()
        Profile.objects.get(user=user)
        self.assertEqual(user.first_name,'John')
        self.assertEqual(user.last_name,'Doe')
        self.assertEqual(user.profile.phone,'1234567890')
        self.assertEqual(user.profile.address,'123 Main St')


class TestContactForm(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Casa Donizetti"
        )

    def test_contact_form_create_valid_inquiry(self):
        inquiry_form_response = ContactUsForm(
            data={
                "request_type": "inquiry",
                "name": "Alan Coomey",
                "email": "alan@example.com",
                "phone": "0871234567",
                "message": "I lost my key.",
                "party_size": "",
                "reservation_for": "",
            },
        )

        self.assertTrue(inquiry_form_response.is_valid(), msg="Form is valid")

    def test_contact_form_invalid_inquiry(self):
        inquiry_form_response = ContactUsForm(
            data={
                "request_type": "inquiry",
                "name": "",
                "email": "",
                "phone": "",
                "message": "",
                "party_size": "",
            }
        )

        self.assertFalse(inquiry_form_response.is_valid(), msg="Form is invalid")

    def test_contact_form_create_private_dining_reservation(self):
        reservation_form_response = ContactUsForm(data={
                "request_type": "private_dining",
                "name": "Alan Coomey",
                "email": "alan@example.com",
                "phone": "0871234567",
                "message": "I'd like to book a private room.",
                "party_size": 12,
                "reservation_for": "2026-07-20",
               },
            )

        self.assertTrue(reservation_form_response.is_valid(), msg="Form is valid")

    def test_contact_form_invalid_private_dining_reservation(self):
        reservation_form_response = ContactUsForm(data={
                "request_type": "private_dining",
                "name": "Alan Coomey",
                "email": "alan@example.com",
                "phone": "0871234567",
                "message": "I'd like to book a private room.",
                "party_size": "",
                "reservation_for": "",
               },
            )
        self.assertFalse(reservation_form_response.is_valid(), msg="Form is invalid")
