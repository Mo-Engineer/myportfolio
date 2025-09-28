from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['first_name', 'last_name', 'message', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'shadow form-control form-control-lg',
                'placeholder': 'First Name',
                'id': 'inputFirstName'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'shadow form-control form-control-lg',
                'placeholder': 'Last Name',
                'id': 'inputLastName'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'shadow form-control form-control-lg',
                'placeholder': 'Email Address',
                'id': 'inputEmail'
            }),
            'message': forms.Textarea(attrs={
                'class': 'shadow form-control form-control-lg',
                'placeholder': 'Message',
                'id': 'message',
                'rows': 8
            })
        }
