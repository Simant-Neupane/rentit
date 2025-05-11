from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Property,PropertyImage

# User form (username, email, password)
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Profile form (extra fields like image, dob, etc.)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'desc', 'dob']

        widgets = {
            'dob' : forms.DateInput(attrs={'type':'date'})
        }

class PropertyUpload(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title','category','perportyType','price','location','disc']




    