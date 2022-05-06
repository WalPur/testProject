from django.views.generic import ListView

from web.models import Tournament


class TournamentListView(ListView):
    model = Tournament
    template_name = "index.html"
