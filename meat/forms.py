from django import forms

from .models import SystemConfig


class ConfigForm(forms.ModelForm):
    class Meta:
        model = SystemConfig