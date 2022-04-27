from django.shortcuts import render
from rest_framework import generics

from web.models import Tournament
from .serializers import TournamentSerializer

class TournamentAPIView(generics.ListAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

# Create your views here.
