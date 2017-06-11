from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #date_of_birth = models.DateField(blank=True, null=True)

class PublishedManager(models.Manager):
    def get_querysets(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Task(models.Model):

    STATUS_CHOICE = (
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

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='task')        #user jest kluczem obcym w tablei TEST. Kazdy TEST musi byc przypisany do jakiegos usera

    discription = models.CharField(null=True, max_length= 250)                          #krotki opis testu
    created = models.DateTimeField(auto_now=True)                                       #Automatycznie ustawia wartosci kiedy obiekt jest tworzony.
    finished = models.DateTimeField(blank=True, null=True)                              #jesli zakonczone zadanie to wpisz czas zakonczenia
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='running')  #ustawienie statusu zadania

    #Parametry do algorytmu Brutforce:
    hash = models.CharField(max_length=32)
    dictionary = models.PositiveSmallIntegerField(choices=DICTIONARY_CHOICES, default=2)
    max_password_len = models.IntegerField(default=8)


    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-created',)

    def __self__(self):
        return self.author






