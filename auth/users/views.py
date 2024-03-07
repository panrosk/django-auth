from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser as User
from .serializers import CustomUserSerializer as UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class ListCreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@permission_classes([IsAdminUser])
class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@permission_classes([IsAuthenticated])
class DetailUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        # Exclude the 'email' field from the request data
        request_data = request.data.copy()
        request_data.pop('email', None)

        # Serialize the updated data excluding 'email'
        serializer = self.get_serializer(self.request.user, data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        # Save the updated data
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)   
