"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


import sys
sys.path.append('..')

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
