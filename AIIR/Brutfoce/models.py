# coding=utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)


class Task(models.Model):

    STATUS_CHOICE = (
        ('submitted', 'Submitted'),
        ('running', 'Running'),     #zadanie w trakcie
        ('paused', 'Paused'),       #zadanie zatrzymane
        ('ended', 'Ended'),         #zadanie zakonczone
        ('canceled', 'Canceled'),    #zadanie anulowane
    )

    DICTIONARY_CHOICES = (
        (1, 'Wszystkie'),
        (2, 'Cyfry'),
        (3, 'Małe litery'),
        (4, 'Duże litery'),
        (5, 'Wszystkie litery'),
        (6, 'Małe litery i cyfry'),
        (7, 'Duże litery i cyfry'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='task')        #user jest kluczem obcym w tablei TEST. Kazdy TEST musi byc przypisany do jakiegos usera

    description = models.CharField(null=True, max_length= 250)                          #krotki opis testu
    created = models.DateTimeField(auto_now=True)                                       #Automatycznie ustawia wartosci kiedy obiekt jest tworzony.
    finished = models.DateTimeField(blank=True, null=True)                              #jesli zakonczone zadanie to wpisz czas zakonczenia
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='submitted')  #ustawienie statusu zadania

    #Parametry do algorytmu Brutforce:
    hash = models.CharField(max_length=32)
    dictionary = models.PositiveSmallIntegerField(choices=DICTIONARY_CHOICES, default=2)
    max_password_len = models.IntegerField(default=8)
    input_password = models.CharField(max_length=32, default='haslo')
    output_password = models.CharField(max_length=32, default='')

    class Meta:
        ordering = ('-created',)







