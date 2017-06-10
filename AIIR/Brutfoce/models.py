from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #date_of_birth = models.DateField(blank=True, null=True)

class Tasks(models.Model):
    #user jest kluczem obcym w tablei TEST. Kazdy TEST musi byc przypisany do jakiegos usera
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #krotki opis testu
    discription = models.CharField(max_length= 250)

    #Automatycznie ustawia wartosci kiedy obiekt jest tworzony.
    #It must be in ""YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format."
    start_date = models.DateTimeField(auto_now=True)

    #status okreslajacy czy zadanie jest w toku czy nie. True dla zadania ktore jest w toku
    #czyli jak tworzymy test to na starcie dostaje True
    status = models.BooleanField(True)






