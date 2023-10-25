from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='genre_image', null=True , blank=True)
    image = models.ImageField(upload_to='images/', null=True , blank=True)


    def __str__(self):
        return self.name
    

class Publisher (models.Model):
    name= models.CharField(max_length=200, unique=True)
    description= models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='publisher_image', null=True , blank=True)
    image = models.ImageField(upload_to='images/', null=True , blank=True)
    info= models.TextField(null=True , blank=True)
    address= models.TextField(null=True , blank=True)
    phone= models.TextField(null=True , blank=True)
    
    
    def __str__(self):
        return self.name
    

class Autor (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_data = models.DateField(null=True , blank= True)
    death_data = models.DateField(null=True , blank=True)
    gener= models.ManyToManyField(Genre)
    info= models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='autor_image', null=True , blank=True)
    image = models.ImageField(upload_to='images/', null=True , blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Book (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='book_image', null=True , blank=True)
    image = models.ImageField(upload_to='images/', null=True , blank=True)
    info= models.TextField(null=True , blank=True)
    price= models.IntegerField(null=True , blank=True)
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE)
    publisher= models.ForeignKey(Publisher, on_delete=models.CASCADE)
    gener= models.ManyToManyField(Genre)
    def __str__(self):
        return self.title


#Returns an array of all users
class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


class User_id(models.Model):
    user_id = models.IntegerField(null=True , blank=True)
    def __str__(self):
        return str(self.user_id)
# Create your models here.
