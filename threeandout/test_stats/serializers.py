
from django.forms import widgets
from rest_framework import serializers
from test_stats.models import NFLPlayer, NFLWeeklyStat #, LANGUAGE_CHOICES, STYLE_CHOICES


class NFLPlayerSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField()
    #name = serializers.CharField(max_length=200)
    #team = serializers.CharField(max_length=200)
    #position = serializers.CharField(max_length=2)
    class Meta:
        model = NFLPlayer
        fields = ('id', 'name', 'team', 'position')

class NFLWeeklyStatSerializer(serializers.ModelSerializer):
    ##week = serializers.IntegerField()
    #score = serializers.FloatField()
    #recTd = serializers.IntegerField()
    #recYds = serializers.IntegerField()
    #fumbles = serializers.IntegerField()
    #interceptions = serializers.IntegerField()
    #passTd = serializers.IntegerField()
    #passYds = serializers.IntegerField()
    #fumbleRecoveryTDs = serializers.IntegerField()
    #rushYds = serializers.IntegerField()
    #rushTd = serializers.IntegerField()
    #player = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = NFLWeeklyStat
        fields = ('id', 'week', 'score', 'recTd', 'recYds', 'fumbles', 'interceptions',
              'passTd', 'passYds', 'fumbleRecoveryTDs', 'rushYds', 'rushTd', 'player')
   
