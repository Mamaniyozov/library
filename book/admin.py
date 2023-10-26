from django.contrib import admin

from .models import Genre, Publisher, Author, Book, User ,User_id , login_user ,Language  ,Reaction

# admin.site.register(User)

admin.site.register(Genre)

admin.site.register(User)

admin.site.register(Publisher)

admin.site.register(Author)

admin.site.register(User_id)

admin.site.register(Book)

admin.site.register(Language)

admin.site.register(login_user)

admin.site.register(Reaction)
# Register your models here.
