from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordResetForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        error_messages={'required': 'Username is Required and Not give any space Letters, digits and @/./+/-/_ only.'},
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )

    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'First Name is Required'},
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'Last Name is Required'},
    )

    email = forms.EmailField(
        label="Email",
        error_messages={'required': 'Email is Required'},
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is Required'},
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        error_messages={'required': 'Confirm password is Required'},
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class':'form-control','id':'ibtn'}),
        error_messages={'required': 'Username is Required',
                        'invalid_login': 'Invalid username or password.',}
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control','id':'ibtn'}),
        error_messages={'required': 'Password is Required',
                        'invalid_login': 'Invalid username or password.'}
    )
    
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
    label=_("Email"),
    max_length=254,
    widget=forms.EmailInput(attrs={"autocomplete": "email", 'class':'form-control', 'id':'ibtn'}),
    error_messages={'required': 'Email is Required'}
)
    
    
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'zipcode', 'state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'ibtn'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'id': 'ibtn'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'id': 'ibtn'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ibtn'}),
            'state': forms.Select(attrs={'class': 'form-control', 'id': 'ibtn'})
        }
        error_messages = {
            'name': {
                'required': 'Name is Required',
            },
            'locality': {
                'required': 'Locality is Required',
            },
            'city': {
                'required': 'City is Required',
            },
            'zipcode': {
                'required': 'Zipcode is Required',
            },
            'state': {
                'required': 'State is Required',
            }
        }

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'class':'form-control', 'id':'ibtn'}
        ),
        required=True,  
        error_messages={
            'required': _("Old password is required."),
        },
    )

    new_password1 = forms.CharField(
        label=_("New Password"),
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'class':'form-control', 'id':'ibtn'}
        ),
        strip=False,
        required=True, 
        error_messages={
            'required': _("New password is required."),
        },
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', 'id':'ibtn'}),
        strip=False,
        required=True,
        error_messages={
            'required': _("Confirm new password is required."),
        },
    )

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', 'id':'ibtn'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control', 'id':'ibtn'}),
    )


    
    