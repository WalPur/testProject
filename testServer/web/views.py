from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Tournament

class TournamentListView(ListView):
    model = Tournament
    template_name = "tournament_list.html"