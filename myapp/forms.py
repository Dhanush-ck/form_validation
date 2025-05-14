from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Enter your name '}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))