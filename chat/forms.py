from django.forms import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoomForm(forms.Form):
    name = fields.CharField(max_length=30, label="")
    description = fields.CharField(max_length=500, label="")

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'login-field'
        self.fields['description'].widget.attrs['class'] = 'login-field'
        
        self.fields['name'].widget.attrs['placeholder'] = 'Room Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Room Description'

class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'login-field'
        self.fields['email'].widget.attrs['class'] = 'login-field'
        self.fields['password1'].widget.attrs['class'] = 'login-field'
        self.fields['password2'].widget.attrs['class'] = 'login-field'
        
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']