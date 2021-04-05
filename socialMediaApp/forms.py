from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import User, Comment
from .models import Post
from django.contrib.auth.models import User as DjangoUser

from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True)
    phoneNumber = forms.CharField(max_length=255, required=True, label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput, max_length=255, required=True)
    firstName = forms.CharField(max_length=255, required=False, label="First Name")
    lastName = forms.CharField(max_length=255, required=False, label="Last Name")
    gender = forms.CharField(widget=forms.Select(choices=[(None, ''),
                                                          ('male', 'Male'),
                                                          ('female', 'Female')]), required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    website = forms.URLField(widget=forms.URLInput, required=False)
    loginWithPhoneNumber = forms.BooleanField(required=False, label="Login With Phone Number?")


class UserUpdateForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, max_length=255, required=False)
    firstName = forms.CharField(max_length=255, required=False)
    lastName = forms.CharField(max_length=255, required=False)
    gender = forms.CharField(widget=forms.Select(choices=[(None, ''),
                                                          ('male', 'Male'),
                                                          ('female', 'Female')]), required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    website = forms.URLField(widget=forms.URLInput, required=False)


class UserEnterForm(forms.Form):
    username = forms.CharField(required=True, max_length=255)
    password = forms.CharField(required=True, max_length=255, widget=forms.PasswordInput)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'description': forms.Textarea(),
        }
        error_messages = {
            'title': {
                'max_length': _("This Password is too long."),
            },
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'id': 'txtSearch'}))


class tokenForm(forms.Form):
    token = forms.CharField(max_length=255)


class PostCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]
