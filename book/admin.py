from django.contrib import admin

from .models import Genre, Publisher, Author, Book, User

# admin.site.register(User)

admin.site.register(Genre)


admin.site.register(Publisher)

admin.site.register(Author)

admin.site.register(Book)


# Register your models here.
