from allauth.account.forms import LoginForm

class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        for field in self.fields.keys():
            if field != 'remember':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                })
