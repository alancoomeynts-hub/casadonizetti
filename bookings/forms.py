from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):

    reservation_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    TIME_CHOICES=[]

    for i in range(16, 23, 1):
        for j in range(0, 60, 15):
            TIME_CHOICES.append((f"{i}:{j:02d}", f"{i}:{j:02d}"))

    reservation_time=forms.ChoiceField(choices=TIME_CHOICES,
                                       widget=forms.Select(attrs={'class':'form-select'}))

    create_account=forms.BooleanField(required=False)

    password=forms.CharField(widget=forms.PasswordInput,required=False)

    class Meta:
        model = Reservation
        fields = (

            'party_size',
            'reservation_date',
            'reservation_time',
            'contact_name',
            'contact_email',
            'contact_phone',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user and self.user.is_authenticated:
            del self.fields['create_account']
            del self.fields['password']
            del self.fields['contact_phone']
            del self.fields['contact_email']
            del self.fields['contact_name']

