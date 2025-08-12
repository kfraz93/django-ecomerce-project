# puddle/core/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User

# The INPUT_CLASSES constant is no longer needed since we are using the
# centralized 'form-input' class defined in input.css.

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-input'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-input'
    }))
    first_name = forms.CharField(max_length=30, required=False,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'First Name',
                                     'class': 'form-input'
                                 }))
    last_name = forms.CharField(max_length=150, required=False,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Last Name',
                                    'class': 'form-input'
                                }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'form-input'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-input'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'form-input'
    }))


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email Address'
            }),
        }


class MyPasswordResetForm(PasswordResetForm):
    """
    A custom password reset form with Tailwind CSS styling.
    """
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'form-input'
        })
    )


class MySetPasswordForm(SetPasswordForm):
    """
    A custom password setting form with Tailwind CSS styling.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-input'
            })
