# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.shortcuts import render,render_to_response,RequestContext, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
#from django.core.exceptions import DoesNotExist
from datetime import datetime, timedelta
import time
import pytz
from test_stats.models import NFLPlayer, Picks,FFLPlayer,NFLSchedule, NFLWeeklyStat
from test_stats.forms import FFLPlayerForm

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from test_stats.serializers import *

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def rest_list_factory(model, serializer, methods=None):
    '''
        Builds a list RESTful services
        List all objects, or creates a new object
    '''
    def list_func(request):

        if request.method == 'GET':
            objs = model.objects.all()
            serialize = serializer(objs, many=True)
            return JSONResponse(serialize.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serialize = serializer(data=data)
            if serialize.is_valid():
                serialize.save()
                return JSONResponse(serialize.data, status=201)
            else:
                return JSONResponse(serialize.errors, status=400)

    def define_func(request, pk):
        try:
            obj = model.objects.get(pk=pk)
        except model.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serialize = serializer(obj)
            return JSONResponse(serialize.data)

        elif request.method == 'PUT':
            print request.body
            data = JSONParser().parse(request)
            serialize = serializer(obj, data=data)
            if serialize.is_valid():
                serialize.save()
                return JSONResponse(serialize.data)
            else:
                return JSONResponse(serialize.errors, status=400)

        elif request.method == 'DELETE':
            obj.delete()
            return HttpResponse(status=204)

    return csrf_exempt(list_func), csrf_exempt(define_func)

player_list, player_detail = rest_list_factory(NFLPlayer, NFLPlayerSerializer)
fplayer_list, fplayer_detail = rest_list_factory(FFLPlayer, FFLPlayerSerializer)
picks_list, picks_detail = rest_list_factory(Picks, PicksSerializer)
weeklyStats_list, weeklyStats_detail = rest_list_factory(NFLWeeklyStat, NFLWeeklyStatSerializer)
