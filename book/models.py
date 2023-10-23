from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    

class Publisher (models.Model):
    name= models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
    

class Autor (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_data = models.DateField(null=True , blank= True)
    death_data = models.DateField(null=True , blank=True)
    gener= models.ManyToManyField(Genre)
    info= models.TextField(null=True , blank=True)

# Create your models here.
