"""
"""

from django.test import TestCase
from test_stats.serializers import *
from test_stats.models import *

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import StringIO

class JSONTest(TestCase):

    def doSerialize(self, model, serializer):
        obj = model.objects.all()[0]
        serial_data = serializer(obj)
        print serial_data.data

        content = JSONRenderer().render(serial_data.data)
        print content

        stream = StringIO.StringIO(content)
        data = JSONParser().parse(stream)

        serial_data2 = serializer(data=data)
        self.assertTrue(serial_data2.is_valid())

        print serial_data2.object

        serial_data3 = serializer(model.objects.all(), many=True)
        print serial_data3.data
        


    def testNFLPlayer(self):
        
        player = NFLPlayer(name="John Doe", team="Redskins", position="TE")
        player.save()

        player = NFLPlayer(name="Freddie Doe", team="Redskins", position="QB")
        player.save()

        self.doSerialize(NFLPlayer, NFLPlayerSerializer)
        return

    def testNFLWeeklyStat(self):
        player = NFLPlayer(name="John Doe", team="Redskins", position="TE")
        player.save()
        
        stat = NFLWeeklyStat(week=1, score=10.0, recTd=2, recYds=4, fumbles=4, interceptions=3,
              passTd=100, passYds=20, fumbleRecoveryTDs=10, rushYds=44, rushTd=1, player=player)
        stat.save()

        self.doSerialize(NFLWeeklyStat, NFLWeeklyStatSerializer)
        return
