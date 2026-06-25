from django import forms
from django.contrib.auth.models import User
from .models import Profile

class CustomSignupForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    phone=forms.CharField(max_length=15)
    address=forms.CharField(max_length=200, widget=forms.Textarea)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Profile(user=user)
        profile.phone = self.cleaned_data.get('phone','')
        profile.address = self.cleaned_data.get('address','')
        profile.save()




