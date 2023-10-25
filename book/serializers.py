from .models import Book,Author,Genre,User,User_id,Publisher,Language
from rest_framework.serializers import ModelSerializer

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


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class User_idSerilizers(ModelSerializer):
    class Meta :
        model = User_id
