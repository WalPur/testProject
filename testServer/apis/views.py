from rest_framework import generics

from accounts.models import CustomUser
from apis.permissions import IsAdminUserOrReadOnly, IsModOrReadOnly, IsAdminUserAndNotMod
from apis.serializers import TournamentSerializer, UsersSerializers
from web.models import Tournament


class TournamentAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsModOrReadOnly]
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class UsersAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUserAndNotMod]
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializers


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserAndNotMod]
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializers
