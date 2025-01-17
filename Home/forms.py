from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login as login_auth,authenticate

class Register(forms.ModelForm):
    first_name = forms.CharField(label="first_name",required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    # terms = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password!=password2:
            raise forms.ValidationError("Password Mismatch")
        
        if len(password)<=4 :
            raise forms.ValidationError("Password Muse be greater than 4 letters")
        
    class Meta:
        model = User
        fields = ["first_name","username","email","password"]
    
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None :
            raise forms.ValidationError("User not Found")