# coding=utf-8
from django import forms
from .models import Task
from django.contrib.auth.models import User

from django import forms

DICTIONARY_CHOICES = (
        (1, 'Wszystkie'),
        (2, 'Cyfry'),
        (3, 'Małe litery'),
        (4, 'Duże litery'),
        (5, 'Wszystkie litery'),
        (6, 'Małe litery i cyfry'),
        (7, 'Duże litery i cyfry'),
    )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password doesn\'t match.')
        return cd['password2']


class TestForm(forms.ModelForm):

    input_password = forms.CharField(label='input_password', required=True, max_length=32)
    dictionary = forms.ChoiceField(required=True, choices=DICTIONARY_CHOICES, initial=2)

    class Meta:
        model = Task
        fields = ('description', 'input_password', 'max_password_len', 'dictionary')

