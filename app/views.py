from logging import raiseExceptions
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User

# Create your views here.
# class RegisterView(APIView):
#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data) 
#         else:
#             raiseExceptions

class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class LoginView(viewsets.ModelViewSet):


