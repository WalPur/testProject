from django.urls import path 

from .views import TournamentListView

urlpatterns = [
    path('', TournamentListView.as_view(), name='home'),
    path('tournaments', TournamentListView.as_view(), name='home')
]
