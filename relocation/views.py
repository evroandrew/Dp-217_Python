from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import HousingForm
from .services import HousingService as Housings, fill_housings


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
    return JsonResponse(Housings.all_json(), safe=False, json_dumps_params={'ensure_ascii': False})


def parse_housings_view(request):
    fill_housings(request.GET.get('city_name'))
    return redirect('/')
