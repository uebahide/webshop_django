from typing import Any
from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password

class UserRegisterForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class':'border rounded-lg'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'border rounded-lg'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'border rounded-lg'
            }
        )
    )
    confirm_password = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class':'border rounded-lg'
            }
        )
    )


    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'confirm_password')

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password does not match!')
        
    def save(self, commit: bool = False) -> Any:
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
  
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'border rounded-lg'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'border rounded-lg'
            }
        )
    )
    remember = forms.BooleanField(
        label='Remember me',
        required=False
    )