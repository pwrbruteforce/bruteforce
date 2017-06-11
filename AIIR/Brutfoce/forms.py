from django import forms
from .models import Task
import datetime
from django.contrib.auth.models import User


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

class TestForm(forms.Form):
    class Meta:
        model = Task
        fields = ('discription', 'hash', 'dictionary', 'max_password_len')

'''    STATUS_CHOICE = (
        ('running', 'Running'),     #zadanie w trakcie
        ('paused', 'Paused'),       #zadanie zatrzymane
        ('ended', 'Ended'),         #zadanie zakonczone
        ('canceled','Canceled'),    #zadanie anulowane
    )

    DICTIONARY_CHOICES = (
    (1, 'Wszystkie'),
    (2 ,'Cyfry'),
    (3 ,'Male_litery'),
    (4 ,'Duze_litery'),
    (5 ,'Wszystkie_litery'),
    (6 ,'Male_litery_Cyfry'),
    (7 ,'Duze_litery_Cyfry'),
    )

    discription = forms.CharField(required=False, max_length=250)
    hash = forms.CharField(required=True, max_length=32, min_length=32)
    dictionary = forms.ChoiceField(required=True, choices=DICTIONARY_CHOICES, initial=2)
    day = forms.DateTimeField(initial=datetime.date.today)
    max_password_len = forms.IntegerField(required=True, min_value=0, max_value=7)
'''