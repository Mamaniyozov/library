from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializers
from rest_framework.request import Request
from rest_framework.response import Response

        
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def list(self, request:Request, *args, **kwargs):
        user_objs = User.objects.all()
        user = UserSerializers(user_objs, many=True)
        return Response(data=user.data)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    
        
