
from django import forms

class TextForm(forms.Form):
    text1 = forms.CharField(label='text1')
    text2 = forms.CharField(label='text2')
