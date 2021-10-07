from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def index_view(request):
    return render(request, "index.html")


def questioning_view(request):
    return render(request, "questioning.html")


@csrf_exempt
def questioning_ajax(request):
    tmp = json.loads(request.read())
    return render(request, "questioning_ajax.html",
                  {'question': tmp['question'], 'answer_id_1': tmp['answer_id_1'], 'answer_id_2': tmp['answer_id_2'],
                   'values': tmp['values'], 'result_1': tmp['result_1'], 'result_2': tmp['result_2']})
