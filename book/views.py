from django.contrib.auth.models import User
from .serializers import Book,Author,Genre,Users,User_id,Publisher,Language, creat_user, login_user, Reaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
class Users(APIView):
    def get(self, requsets):
        try:
            user = Users.objects.all()
            return Response({"username": user.username, "first_name": user.first_name, "last_name": user.last_name})
        except:
            return Response({'result': ' Users not found'})


class Users_id(APIView):
    def get(self, requsets, id):
        try:
            user = User_id.objects.get(id=id)
            return Response({"username": user.username, "first_name": user.first_name, "last_name": user.last_name})
        except:
            return Response({'result': ' Users not found'})

    def put(self, requsets, id):
        try:
            user = User.objects.get(id=id)
            user.username = requsets.data.get('username')
            user.first_name = requsets.data.get('first_name')
            user.last_name = requsets.data.get('last_name')
            user.save()
            return Response({"username": user.username, "first_name": user.first_name, "last_name": user.last_name})
        except:
            return Response({'result': ' Users not found'})
class Userlogin(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,requsts:Request)->Response :
        user =  requsts.user
        token = Token.objects.get(user=user)
        return Response({"result":token.key}, status=status.HTTP_201_CREATED)