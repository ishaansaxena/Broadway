from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

# Login form, inherited from Django's Auth Form
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Create a form for login
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

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
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

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("name", "bio", "profile_picture",)
