from django.contrib.auth.models import User
from .models import Book,Genre,Language,Author,Publisher, Reaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
class Users(APIView):
    def get(self, requsets):
        try:
            user = User.objects.all()
            return Response({"username": user.username, "first_name": user.first_name, "last_name": user.last_name})
        except:
            return Response({'result': ' Users not found'})
# Create your views here.
