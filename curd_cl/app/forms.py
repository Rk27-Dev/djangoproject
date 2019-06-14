from django import forms
from .models import companymodel

class companyform(forms.ModelForm):
    class Meta:
        model=companymodel
        fields='__all__'