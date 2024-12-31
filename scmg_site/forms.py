# forms.py
from django import forms
from .models import Reading

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = ['id', 'sensor', 'timestamp', 'conductivity', 'depth', 'battery', 'mayfly_temp','signal_percent']