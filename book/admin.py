from django.contrib import admin

from .models import Genre, Publisher, Author, Book, login_user ,Language  ,Reaction
from django.contrib.auth.models import Group

# admin.site.register(User)

admin.site.register([Genre,
                    Publisher, 
                    Author,
                    Book, 
                    login_user ,
                    Language  ,
                    Reaction])
admin.site.unregister(Group)

