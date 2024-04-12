from django import forms
from .models import Log

class solicitudForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = [
            'id',
            'level',
            'message',
            'created'
            'user'
            'time'
        ]

        labels = {
            'id': 'id',
            'level': 'level',
            'message' : 'message',
            'created' : 'created',
            'user': 'user',
            'time': 'time'
        }