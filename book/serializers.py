from .models import Book,Author,Genre,Publisher,Language, creat_user, login_user, Reaction
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class AutorSerializers(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        

class GenerSerializers(ModelSerializer):
    class Meta:
        modol = Genre
        fields = "__all__"


class BookSerializers(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class LanguageSerializers(ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class PublisherSerializers(ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class ReactionSerializers(ModelSerializer):
    class Meta:
        model = Reaction
        fields = "__all__"


class Creat_userSerializers(ModelSerializer):
    class Meta:
        model = creat_user
        fields = "__all__"

class Login_userSerializers(ModelSerializer):
    class Meta:
        model = login_user
        fields = "__all__"

