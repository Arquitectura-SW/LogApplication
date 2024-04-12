from django import forms
from .models import Log

class solicitudForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = [
            'level',
            'message',
            'created'
            'user'
            'time'
        ]

        labels = {
            'level': 'level',
            'message' : 'message',
            'created' : 'created',
            'user': 'user',
            'time': 'time'
        }