from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User



class postForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":3, "placeholder": "descriptions"}))

    class Meta:
        model = Post
        fields = ('title', 'body', 'Categories', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "enter title"}),
            
           
        }

class CommentForm(forms.Form):
    
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
        )
    

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2',)

        widgets = {
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder': 'Email Address'})
    
    }    