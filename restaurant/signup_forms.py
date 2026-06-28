from django import forms
from .models import Profile
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    first_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Enter your first name',}))
    last_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Enter your last name',}))
    phone=forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder':'Enter your phone number',}))
    address=forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows':4, 'placeholder':'Enter your address',}))

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })


    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Profile(user=user)
        profile.phone = self.cleaned_data.get('phone','')
        profile.address = self.cleaned_data.get('address','')
        profile.save()



