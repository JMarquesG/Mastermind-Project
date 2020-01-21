from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import GameSerializer, PlaySerializer
from .models import Game,Play

# Create your views here.


class CreateGame(APIView):
    def get(self,request):
        gamelist = [(game.id,game.name)  for  game in Game.objects.all()]
        return Response(gamelist)
    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KeyTest(APIView):
    def post(self,request):
        serializer = PlaySerializer(data = request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class KeyHistory(APIView):
    def get(self,request):
        id = request.data.get('id')
        if id is not None :
            playlist = [(play.c1,play.c2,play.c3,play.c4,play.keys()) for play in Play.objects.filter(game_id = id) ]
            return Response(playlist)
        return 'Not existing Game'