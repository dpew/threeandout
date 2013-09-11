
from django.forms import widgets
from rest_framework import serializers
from test_stats.models import NFLPlayer #, LANGUAGE_CHOICES, STYLE_CHOICES


class NFLPlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    team = serializers.CharField(max_length=200)
    position = serializers.CharField(max_length=2)
