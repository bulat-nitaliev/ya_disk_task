from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import  MyTokenObtainPairSerializer, UserRegistrationSerializer, UserListSerializer
from api.models import User
import requests
from rest_framework.response import Response


class UserViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    def get_serializer_class(self):
        if self.action == 'create':
           return UserRegistrationSerializer
        return UserListSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class YaDiskApiViw(APIView):

    def get(self, request):
        p_k = request.GET.get('arg')
        public = f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={p_k}'
        res = requests.get(public)
        if res.status_code == 200:
            return Response({'res': res.json()})

