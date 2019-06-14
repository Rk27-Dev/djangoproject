from django import forms
class Additem(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()