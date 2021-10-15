from django.shortcuts import render
from django.http import JsonResponse
from .models import Region, City, StudyField, Speciality


def get_json_regions_data(request):
    region_values = list(Region.objects.values())
    return JsonResponse({'data': region_values})


def get_json_cities_data(request, *args, **kwargs):
    selected_region = kwargs.get('region')
    cities_values = list(City.objects.filter(region__name=selected_region).values())
    return JsonResponse({'data': cities_values})


def get_json_fields_data(request):
    values = list(StudyField.objects.values())
    return JsonResponse({'data': values})


def get_json_specs_data(request, *args, **kwargs):
    selected_field = kwargs.get('field')
    specs_values = list(Speciality.objects.filter(study_field__name=selected_field).values())
    return JsonResponse({'data': specs_values})


def uni_search(request):
    return render(request, 'universearch/search_form.html')

