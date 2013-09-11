"""
"""

from django.test import TestCase
from test_stats.serializers import *
from test_stats.models import *

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import datetime

import StringIO

class JSONTest(TestCase):

    def doSerialize(self, model, serializer):
        obj = model.objects.all()[0]
        serial_data = serializer(obj)

        content = JSONRenderer().render(serial_data.data)
        ncontent = content.replace('Doe', 'Don')
        ncontent = ncontent.replace('44', '45')
        print ncontent

        stream = StringIO.StringIO(ncontent)
        data = JSONParser().parse(stream)

        serial_data2 = serializer(obj, data=data)
        self.assertTrue(serial_data2.is_valid())
        serial_data2.save(force_update=True)


        serial_data3 = serializer(model.objects.all(), many=True)
        return serial_data2.object


    def testNFLPlayer(self):
        
        player = NFLPlayer(name="John Doe", team="Redskins", position="TE")
        player.save()
        player.team = "skins"
        player.save()

        player2 = NFLPlayer(name="Freddie Doe", team="Redskins", position="QB")
        player2.save()

        p = self.doSerialize(NFLPlayer, NFLPlayerSerializer)
        p2 = NFLPlayer.objects.get(id=player.id)
        self.assertEquals(p2, p)
        self.assertEquals(p2.name, p.name)

    def testNFLWeeklyStat(self):
        player = NFLPlayer(name="John Doe", team="Redskins", position="TE")
        player.save()
        
        stat = NFLWeeklyStat(week=1, score=10.0, recTd=2, recYds=4, fumbles=4, interceptions=3,
              passTd=100, passYds=20, fumbleRecoveryTDs=10, rushYds=44, rushTd=1, player=player)
        stat.save()

        stat2 = NFLWeeklyStat(week=2, score=12.2, recTd=5, recYds=4, fumbles=4, interceptions=4,
              passTd=100, passYds=20, fumbleRecoveryTDs=15, rushYds=54, rushTd=12, player=player)
        stat2.save()

        val = self.doSerialize(NFLWeeklyStat, NFLWeeklyStatSerializer)
	gold = NFLWeeklyStat.objects.get(id=stat.id)
        self.assertEquals(gold.rushYds, val.rushYds)
#        print dir(stat)
#        print dir(val)

    def testPicks(self):
        user = User(username="bar", password="whatever")
        user.save()
        player = FFLPlayer(user=user, teamname="Redskins", email="Foobar", league=0)
        player.save()

        teplayer = NFLPlayer(name="Tightty", team="Redskins", position="TE")
        teplayer.save()
        qbplayer = NFLPlayer(name="Quarty", team="Redskins", position="QB")
        qbplayer.save()
        wrplayer = NFLPlayer(name="Widey", team="Redskins", position="WR")
        wrplayer.save()
        rbplayer = NFLPlayer(name="Runny", team="Redskins", position="RB")
        rbplayer.save()

        pick = Picks(fflPlayer=player, week=1, qb=qbplayer, rb=rbplayer, te=teplayer, wr=wrplayer, mod_time=datetime.datetime.now())
        pick.save()

        pick = Picks(fflPlayer=player, week=2, qb=qbplayer, rb=rbplayer, te=teplayer, wr=wrplayer, mod_time=datetime.datetime.now())
        pick.save()
        
        val = self.doSerialize(Picks, PicksSerializer)
	gold = Picks.objects.get(id=pick.id)
        self.assertEquals(gold.te, val.te)

    def testFFLPlayer(self):
        user = User(username="bar", password="whatever")
        user.save()

        player = FFLPlayer(user=user, teamname="Redskins", email="Foobar", league=0)
        player.save()
        
        val = self.doSerialize(FFLPlayer, FFLPlayerSerializer)
	gold = FFLPlayer.objects.get(id=player.id)
        self.assertEquals(gold.teamname, val.teamname)
#        print dir(stat)
#        print dir(val)
