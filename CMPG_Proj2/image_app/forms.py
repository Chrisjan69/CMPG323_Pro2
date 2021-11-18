from django import forms
from image_app.models import User
from django.contrib.auth.models import User



class NewUserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
     class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')
