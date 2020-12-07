from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('leaderboard', views.leaderBoard),
    path('show/<rank>', views.show),
    path('enter', views.enter),
    path('changeRanks', views.changeRanks),
    path('logout', views.logout),
]