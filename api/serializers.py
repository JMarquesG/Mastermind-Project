from rest_framework import serializers

from .models import Game,Play

class GameSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    c1 = serializers.CharField()
    c2 = serializers.CharField()
    c3 = serializers.CharField()
    c4 = serializers.CharField()

    def create(self,validate_data):
        instance = Game()
        instance.name = validate_data.get('name')
        instance.c1 = validate_data.get('c1')
        instance.c2 = validate_data.get('c2')
        instance.c3 = validate_data.get('c3')
        instance.c4 = validate_data.get('c4')
        instance.save()
        return instance

    class Meta:
        model = Game
        fields = ('id','name','c1','c2','c3','c4')

class PlaySerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all().values_list('id', flat=True))
    c1 = serializers.CharField()
    c2 = serializers.CharField()
    c3 = serializers.CharField()
    c4 = serializers.CharField()

    def create(self,validate_data):
        instance = Play()
        instance.game_id = validate_data.get('game')
        instance.c1 = validate_data.get('c1')
        instance.c2 = validate_data.get('c2')
        instance.c3 = validate_data.get('c3')
        instance.c4 = validate_data.get('c4')
        instance.save()
        return instance.keys()

    class Meta:
        model = Play
        fields = ('game','c1','c2','c3','c4')
