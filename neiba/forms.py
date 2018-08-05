from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,NeighbourHood,Post,Social,Business

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'photo','gender','house','contribution')
        exclude = ['user']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['hood', 'user']


class NewHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ('name', 'location', 'occupants','city')


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['hood', 'user']

class NewSocialForm(forms.ModelForm):
    class Meta:
        model = Social
        exclude = ['hood']
