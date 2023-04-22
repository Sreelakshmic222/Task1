from django.contrib.auth import login
from knox.models import AuthToken

from .models import Profile
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.db.models import Q # for search method
from django.http import JsonResponse
import json
from rest_framework.views import APIView
# Create your views here.

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data,"token": AuthToken.objects.create(user)[1]
        })

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'

    def get(self, request):
        # Your view logic here
        return Response({'message': 'Hello World!'})

class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        # Your view logic here
        return Response({'message': 'Hello World!'})

class HomePageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'

    def get(self, request):
        # Your view logic here
        return Response({'message':'homepage'})