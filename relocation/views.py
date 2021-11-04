from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .forms import HousingForm, Housings


def get_housings_view(request):
    try:
        form = HousingForm(request.POST)
        return render(request, 'relocation/main.html', {'form': form, 'houses': form.get_housings()})
    except TypeError as e:
        print(e)
    return redirect('/')


def get_housings_view_2(request):
    return render(request, 'relocation/main2.html')


def get_housings_json(request):
    data = json.dumps(Housings.all_json())
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
