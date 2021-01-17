from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Inform a valid email address.'
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'avatar',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
