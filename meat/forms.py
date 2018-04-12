from django import forms

from .models import SystemConfig, CollectInfo


class ConfigForm(forms.ModelForm):
    class Meta:
        model = SystemConfig
        exclude = []


class SGForm(forms.ModelForm):
    class Meta:
        model = CollectInfo
        exclude = ['state', 'flow_step', 'sg_no']