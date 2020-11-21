from django import forms
from formulaire.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = get_user_model()
        fields = ('first_name','last_name','password','email')
        #labels = { 'username': ('Nom utilisateur '), }
        #help_texts = { 'username': (''), }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nom','class':'form-control','required': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Prénom','class':'form-control','required': True}),
            'email': forms.TextInput(attrs={'placeholder': 'Email' ,'class':'form-control'}),
            'password': forms.TextInput(attrs={'placeholder': 'Mot de passe','class':'form-control','type':'password'})
        }

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('photo_profil',)
