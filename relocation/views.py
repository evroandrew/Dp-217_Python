import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import HousingForm
from .models import Housing


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
    housings_objects = Housing.objects.all()
    data = []

    for housing in housings_objects:
        id = housing.id
        if housing.university:
            university_name = housing.university.name
        else:
            university_name = 'none'
        city = housing.city
        city_name = city.name
        housing_name = housing.name
        region_name = housing.city.region.name

        data.append({
            'id': id,
            'housing_name': housing_name,
            'university_name': university_name,
            'city_name': city_name,
            'region_name': region_name
        })
    response = json.dumps(data)
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
