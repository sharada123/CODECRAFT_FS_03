from .models import CustomUser
from django import forms
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','password','confirm_password','mobile','appartment','street','area','pincode']
        widgets={
                'first_name':forms.TextInput(attrs={'class':'form-control mt-2 ','placeholder':'First Name'}),
                'last_name':forms.TextInput(attrs={'class':'form-control mt-2 ','placeholder':'Last Name'}),
                'username':forms.TextInput(attrs={'class':'form-control mt-2 ','placeholder':'username'}),
                'email':forms.EmailInput(attrs={'class':'form-control mt-2 ','placeholder':'email'}),
                'password':forms.PasswordInput(attrs={'class':'form-control mt-2 ','placeholder':'password'}),
                'confirm_password':forms.PasswordInput(attrs={'class':'form-control mt-2 ','placeholder':'confirm password'}),
                'mobile':forms.TextInput(attrs={'class':'form-control mt-2 ','placeholder':'mobile'}),
                'area':forms.Select(choices=CustomUser.area_choices,attrs={'class':'form-control mt-2 ','placeholder':'Place'}),
                'appartment':forms.TextInput(attrs={'class':'form-control mt-2 ','placeholder':'appartment'}),
                'street':forms.TextInput(attrs={'class':'form-control mt-2 ','placeholder':'street'}),
                'pincode':forms.TextInput(attrs={'class':'form-control mt-2 ','placeholder':'pincode'}),
        }
    
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Password'})
    )