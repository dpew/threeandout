
from django.forms import widgets
from rest_framework import serializers
from test_stats.models import NFLPlayer, NFLWeeklyStat #, LANGUAGE_CHOICES, STYLE_CHOICES


class NFLPlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    team = serializers.CharField(max_length=200)
    position = serializers.CharField(max_length=2)
    class Meta:
        model = NFLPlayer
        fields = ('name', 'team', 'position')

class NFLWeeklyStatSerializer(serializers.Serializer):
    week = serializers.IntegerField()
    score = serializers.FloatField()
    recTd = serializers.IntegerField()
    recYds = serializers.IntegerField()
    fumbles = serializers.IntegerField()
    interceptions = serializers.IntegerField()
    passTd = serializers.IntegerField()
    passYds = serializers.IntegerField()
    fumbleRecoveryTDs = serializers.IntegerField()
    rushYds = serializers.IntegerField()
    rushTd = serializers.IntegerField()
    player = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = NFLWeeklyStat
   
