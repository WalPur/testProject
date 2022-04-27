from django.urls import path 

from .views import TournamentAPIView

urlpatterns = [
    path("", TournamentAPIView.as_view(), name='tournament_list'),
]
