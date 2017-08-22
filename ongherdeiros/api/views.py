from django.http import HttpResponse
from django.views import generic
from django.core import serializers
from .models import Evento, DonateItem
import datetime
import json


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the API ONG Herdeiros index.")


def time_converter(o):
    if isinstance(o, datetime.datetime):
        return o.strftime('%d/%m/%Y - %H:%M')


def list_events(request):
    raw_events = serializers.serialize('python', Evento.objects.all())
    rtn = [d['fields'] for d in raw_events]
    return HttpResponse(json.dumps(rtn, default=time_converter))


def list_itens(request):
    raw_itens = serializers.serialize('python', DonateItem.objects.all())
    rtn = [d['fields'] for d in raw_itens]
    return HttpResponse(json.dumps(rtn))
