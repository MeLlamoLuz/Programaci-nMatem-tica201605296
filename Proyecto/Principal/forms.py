from django import forms

from .models import Regex


class RegexForm(forms.ModelForm):
    class Meta:
        model = Regex
        fields = ('expresion',)
