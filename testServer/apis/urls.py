from django.urls import path 

from .views import TournamentAPIView, TournamentDetail, UsersAPIView, UsersDetail

urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users_list'),
    path('users/<int:pk>/', UsersDetail.as_view(), name='users_list'),
    path("tournaments/", TournamentAPIView.as_view(), name='tournament_list'),
    path("tournaments/<int:pk>/", TournamentDetail.as_view(), name="tournament_detail"),
]
