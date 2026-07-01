from .models import ContactRequest
from django import forms

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('request_type','name','email','phone','message','party_size','reservation_for')
        widgets = {
            'request_type': forms.Select(attrs={'class':'form-select'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control','rows':4, 'placeholder':'Enter your message'}),
            'party_size': forms.NumberInput(attrs={'class':'form-control'}),
            'reservation_for': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }