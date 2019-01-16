from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'name',
            'email',
            'position',
            'company',
            'phone',
            'isPublic',
            'user'
        ]
