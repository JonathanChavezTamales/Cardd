from django import forms
from .models import User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = [
            'date_created',
            'isPremium'
        ]
