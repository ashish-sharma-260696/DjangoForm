from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    url = forms.URLField()
    text = forms.CharField(widget=forms.Textarea)
