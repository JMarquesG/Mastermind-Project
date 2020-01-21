from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path(
        'create_game', 
        views.CreateGame.as_view()),
    path(
        'code',
        views.KeyTest.as_view()),
    path('code_history',
        views.KeyHistory.as_view())
]