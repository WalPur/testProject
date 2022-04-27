from django.urls import path 

from .views import TournamentAPIView, TournamentDetail, UsersAPIView, UsersDetail

urlpatterns = [
    path("<int:pk>/", TournamentDetail.as_view(), name="tournament_detail"),
    path("", TournamentAPIView.as_view(), name='tournament_list'),
    path('users/', UsersAPIView.as_view(), name='users_list'),
    path('users/<int:pk>/', UsersDetail.as_view(), name='users_list')
]
