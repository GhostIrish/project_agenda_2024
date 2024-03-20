from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    
    class Meta:
        model = models.Contact
        fields = ('first_name',
                  'last_name',
                  'phone',
                  'email',
                  'description',
                  'category',
                  'picture',
                  ) 
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b',
                    'placeholder': 'Write here'
                }
            ),
            
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Write here'
                }
            ),
            
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Write here'
                }
            ),
            
            'email': forms.TextInput(
                attrs={
                    'class': 'classe-a classe-b',
                    'placeholder': 'Write here'
                }
            )
            
        }
    def clean(self):       
        cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError(
                    'First and last name cannot be the same.',
                    code='invalid'
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        
        return super().clean()

class RegisterForm(UserCreationForm):
    ...