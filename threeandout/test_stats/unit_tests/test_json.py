"""
"""

from django.test import TestCase
from test_stats.serializers import NFLPlayerSerializer
from test_stats.models import NFLPlayer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import StringIO

class JSONTest(TestCase):


    def testNFLPlayer(self):
        
        player = NFLPlayer(name="John Doe", team="Redskins", position="TE")
        player.save()

        serializer = NFLPlayerSerializer(player)
        print serializer.data

        content = JSONRenderer().render(serializer.data)
        print content

        stream = StringIO.StringIO(content)
        data = JSONParser().parse(stream)

        serializer = NFLPlayerSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        print serializer.object

        serializer = NFLPlayerSerializer(NFLPlayer.objects.all(), many=True)
        print serializer.data
