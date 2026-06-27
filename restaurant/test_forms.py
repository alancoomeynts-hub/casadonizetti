from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CustomSignupForm
from .models import Profile

class TestCustomSignupForm(TestCase):

    """
    Unit test class to verify the functionality of the CustomSignupForm.

    This class contains test cases for valid and invalid form data,
    and proper user and profile creation with AllAuth.

    """
    def test_signup_form(self):
        form = CustomSignupForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'address': '123 Main St',

        })

        self.assertTrue(form.is_valid())

    def test_signup_form_invalid(self):
        form = CustomSignupForm(data={
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


