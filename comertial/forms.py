from django import forms
from .models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'description']
    widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name or Company'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'placeholder': 'example@mail.com'
                }),
            'description': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Description'
                }),
        }
