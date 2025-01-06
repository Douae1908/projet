from distutils.log import error
from django import forms

from django.core.validators import RegexValidator, FileExtensionValidator
from django.urls import URLPattern
from .models import Register
from django.forms.widgets import NumberInput

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django import forms
from django.core.validators import RegexValidator, FileExtensionValidator
from apps.authentication.models import Register

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "First Name",
        "class": "form-control"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Last Name",
        "class": "form-control"
    }))
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control"
    }))
    confirmPassword = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm Password",
        "class": "form-control"
    }))
    phone = forms.CharField(
        label="Phone Number",
        validators=[
            RegexValidator(
                r'^\+?[0-9]{7,15}$',  # Permet les numéros internationaux avec "+" en option et 7-15 chiffres.
                message="Enter a valid phone number (e.g., +123456789)."
            )
        ],
        widget=forms.TextInput(attrs={
            "placeholder": "Phone Number",
            "class": "form-control"
        })
    )
    image = forms.ImageField(label="Profile Image", required=False, validators=[
        FileExtensionValidator(['jpg', 'png', 'jpeg'])
    ], widget=forms.FileInput(attrs={
        "class": "form-control"
    }))

    class Meta:
        model = Register
        fields = ('first_name', 'last_name', 'email', 'password', 'phone', 'image')

    def clean_email(self):
        """Validate email uniqueness."""
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_phone(self):
        """Validate phone uniqueness."""
        phone = self.cleaned_data.get('phone')
        if Register.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Phone number already exists.")
        return phone

    def clean(self):
        """Validate passwords match."""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirmPassword')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirmPassword', "Passwords do not match.")



class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200, help_text='Required',widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control"
    }))


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        
        widget=forms.TextInput(
        attrs={
            "placeholder": "First Name",
            "class": "form-control",
      
        }),
        min_length=2,
        max_length=10,
       
    )
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Last Name",
            "class": "form-control"
        }),
        min_length=2,
        max_length=10,
        )
    phone = forms.CharField(
        label="Phone Number",
        validators=[
            RegexValidator(
                r'^\+?[0-9]{7,15}$',  # Allows international phone numbers with optional "+" and 7-15 digits.
                message="Enter a valid phone number (e.g., +123456789)."
            )
        ],
        widget=forms.TextInput(attrs={
            "placeholder": "Phone Number",
            "class": "form-control"
        })
    )
    image = forms.ImageField(required=False, label="profile image", validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], widget=forms.FileInput(attrs={
        "placeholder": "Profile Image",
        "class": "form-control"
    }))
    password = forms.CharField(required=False,widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control"
    }))
    #TODO:add regex to password
    confirmPassword = forms.CharField(required=False,label="confirm password", widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm Password",
        "class": "form-control"
    }))
    country = forms.CharField(required=False,validators=[RegexValidator(
        '^[A-Za-z]+$', message="Enter a Valid Country Name")],widget=forms.TextInput(
        attrs={
            "placeholder": "Country",
            "class": "form-control"
        }))
    birthdate = forms.DateField(required=False,
        widget=NumberInput(
            attrs={
                'placeholder': 'BirthDate',
                'type': 'date',
                'class': 'form-control'
            }
        ))
    facebook_profile = forms.URLField(required=False, error_messages={'required': 'Please Enter a valid Url'},widget=forms.URLInput(
        attrs={
                'placeholder': 'Profile Facebook Url',
                'class': 'form-control'
            }
    ))


    def clean(self):
        errors = {}
        cleaned_data = super().clean()
        valpassword = self.cleaned_data.get('password')
        valconfirmpassword = self.cleaned_data.get("confirmPassword")
        if valpassword != valconfirmpassword:
            errors['confirmPassword'] = ('password not match')  
        phone = self.cleaned_data.get('phone')
        if Register.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
            errors['phone'] = ("phone exists")
     
   
        if errors:
            raise forms.ValidationError(errors)

    class Meta:
        model = Register
        fields = ('first_name','last_name','phone','image','country' , 'password', 'confirmPassword','birthdate','facebook_profile')
        

class ResetPasswordEmailForm(forms.Form):
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "form-control"
    }))

class ResetPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control"
    }))
    #TODO:add regex to password
    confirmPassword = forms.CharField(label="confirm password", widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm Password",
        "class": "form-control"
    }))
    def clean(self):
        errors = {}
        cleaned_data=super().clean()
        valpassword=self.cleaned_data.get('password')
        valconfirmpassword=self.cleaned_data.get("confirmPassword")
        if valpassword != valconfirmpassword:
             errors['confirmPassword'] =  ('password not match')
        if errors:
            raise forms.ValidationError(errors)

    class Meta:
        model = Register
        fields = ('password', 'confirmPassword')
        
class DeleteAccountForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control"
    }))