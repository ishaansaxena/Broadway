from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                widget = field.widget
                if type(widget) is forms.TextInput:
                    # something
                    pass
                elif type(widget) is forms.Textarea:
                    # widget.attrs['class'] = 'form-control'
                    pass
                widget.attrs['placeholder'] = field.label
