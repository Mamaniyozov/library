from django.contrib import admin

from .models import Genre, Publisher, Author, Book, Users ,User_id , login_user ,Language  ,Reaction

# admin.site.register(User)

admin.site.register([Genre,
                    Publisher, 
                    Author,
                    Book, 
                    Users ,
                    User_id , 
                    login_user ,
                    Language  ,
                    Reaction])

