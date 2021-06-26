
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Username :')
    email = forms.EmailField(required=True)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("Email is already registered")
        return self.cleaned_data['email']

    password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={}),)
    password2  = forms.CharField(label=("Confirm"), strip=False, widget=forms.PasswordInput(attrs={}),)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')