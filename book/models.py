from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username, self.user.lastname

class User_id(models.Model):
    user_id = models.IntegerField(null=True , blank=True)
    def __str__(self):
        return str(self.user_id)

class creat_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname, self.lastname, self.email, self.password
    
class login_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname, self.lastname, self.email, self.password


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='genre_image', null=True , blank=True)
    image = models.ImageField(upload_to='images/', null=True , blank=True)


    def __str__(self):
        return self.name

    
class Author (models.Model):
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


class Language(models.Model):
    name = models.CharField(max_length=200, unique=True)

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

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='book_image', null=True , blank=True)
    image = models.ImageField(upload_to='images/', null=True , blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    info= models.TextField(null=True , blank=True)
    price= models.IntegerField(null=True , blank=True)
    year= models.IntegerField(null=True , blank=True)
    pages= models.IntegerField(null=True , blank=True)
    isbn= models.IntegerField(null=True , blank=True)
    count= models.IntegerField(null=True , blank=True)
    

class Reaction(models.Model):
    like = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
