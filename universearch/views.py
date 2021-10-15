from django.shortcuts import render
from django.http import JsonResponse
from .models import Region, City, StudyField
from .pars import get_cities, get_regions, SITE_URL


def populate_db_regions():
    regions = get_regions(SITE_URL)
    for region in regions:
        reg = Region(name=region)
        reg.save()


def populate_db_cities():
    cities_li = get_cities(SITE_URL)
    for region, cities in cities_li.items():
        region = Region.objects.filter(name=region).first()

        for city in cities:
            city_obj = City(name=city, region=region)
            city_obj.save()


def get_json_regions_data(request):
    region_values = list(Region.objects.values())
    return JsonResponse({'data': region_values})


def get_json_cities_data(request, *args, **kwargs):
    selected_region = kwargs.get('region')
    if selected_region == 'Всi областi':
        cities_values = list(City.objects.values())
    else:
        cities_values = list(City.objects.filter(region__name=selected_region).values())
    return JsonResponse({'data': cities_values})


def get_json_fields_data(request):
    values = list(StudyField.objects.values())
    return JsonResponse({'data': values})


def uni_search(request):
    # regs = Region.objects.all()
    # cities = City.objects.all()
    #
    # if not regs:
    #     populate_db_regions()
    # if not cities:
    #     populate_db_cities()
    return render(request, 'uni_search.html')