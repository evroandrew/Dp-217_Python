from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
import json


def index_view(request):
    return render(request, "index.html")


def questioning_view(request):
    return render(request, "questioning.html")


@csrf_exempt
def questioning_ajax(request):
    tmp = json.loads(request.read())
    t = loader.get_template('questioning_ajax.html')
    return HttpResponse(t.render(tmp, request))

@csrf_exempt
def questioning_results(request):
    tmp = json.loads(request.read())
    t = loader.get_template('questioning_results.html')
    return HttpResponse(t.render(tmp, request))