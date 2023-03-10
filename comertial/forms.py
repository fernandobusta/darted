from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactEmail
        fields = ['email']
    
        widgets = {
            'email': forms.EmailInput(attrs={
                    'class': "form-control",
                    'placeholder': 'Enter your Email...',
                    }),
        }

class JoinTeamForm(forms.ModelForm):
    class Meta:
        model = JoinTeam    
        fields = ['name', 'email', 'city', 'other']
        
        
        widgets = {
                'name': forms.TextInput(attrs={
                    'class': "form-control",
                    'placeholder': 'Enter your Name...'
                    }),
                'email': forms.EmailInput(attrs={
                    'class': "form-control", 
                    'placeholder': 'Enter your Email...'
                    }),
                'city': forms.TextInput(attrs={
                    'class': "form-control",
                    'placeholder': 'City of residence'
                    }),
                'other': forms.TextInput(attrs={
                    'class': "form-control",
                    'placeholder': 'Other info (Optional)'
                    }),
            }
    