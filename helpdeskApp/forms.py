from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User



class ReportedDeviceForm(ModelForm):
    class Meta:
        model = ReportedDevices
        fields = ['device_type', 'device_serial', 'device_issue_description']
        exclude = ['device_origin', ]
        message = forms.CharField(widget=forms.Textarea, max_length=2000)
