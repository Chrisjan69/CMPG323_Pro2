from django import forms
from image_app.models import User
from django.contrib.auth.models import User
from django import forms
from . import models



class NewUserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
     class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')




class ImageForm(forms.ModelForm):
   class Meta:
      model=models.UserImage
      fields=['title', 'desc']
