from django import forms
from django.forms import fields
from .models import signupuser, userform

class signupForm(forms.ModelForm):
    class Meta:
        model=signupuser
        fields='__all__'

class userformdata(forms.ModelForm):
    class Meta:
        model=userform
        fields='__all__'