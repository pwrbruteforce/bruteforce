from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #date_of_birth = models.DateField(blank=True, null=True)

class Tasks(models.Model):

    STATUS_CHOICE = (
        ('running', 'Running'),     #zadanie w trakcie
        ('paused', 'Paused'),       #zadanie zatrzymane
        ('ended', 'Ended'),         #zadanie zakonczone
        ('canceled','Canceled'),    #zadanie anulowane
    )


    author = models.ForeignKey(User, on_delete=models.CASCADE)        #user jest kluczem obcym w tablei TEST. Kazdy TEST musi byc przypisany do jakiegos usera
    discription = models.CharField(max_length= 250)                 #krotki opis testu
    created = models.DateTimeField(auto_now=True)                   #Automatycznie ustawia wartosci kiedy obiekt jest tworzony.
    finished = models.DateTimeField(default=timezone.now)           #jesli zakonczone zadanie to wpisz czas zakonczenia
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='running')  #ustawienie statusu zadania

    #Parametry do algorytmu Brutforce:
    hasch = models.CharField(max_length=32)








