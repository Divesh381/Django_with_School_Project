from django import forms

class userForm(forms.Form):
    num1=forms.CharField(label='First Name', required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.CharField(label='Last Name', required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    # num3=forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'class':"form-control"}))