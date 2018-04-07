from django import forms

from .models import bitlyURL

class newForm(forms.ModelForm):
    class Meta:
        model = bitlyURL
        fields = [
            'url'
        ]