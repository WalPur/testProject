from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import *
from rest_framework.response import Response

from web.models import Tournament
from accounts.models import CustomUser
from .serializers import TournamentSerializer, UsersSerializers
from .permissions import IsAdminUserOrReadOnly, IsModOrReadOnly, IsAdminUserAndNotMod

class TournamentAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsModOrReadOnly]
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class UsersAPIView(generics.ListAPIView):
    permission_classes  = [IsAdminUserAndNotMod]
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializers


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes  = [IsAdminUserAndNotMod]
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializers