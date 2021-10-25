from django.http.response import HttpResponse
from .services import (
    CityService as Cities,
    UniversityService as Unies,
    HousingService as Housings,
    Region, City
    )
from .forms import (
    HousingForm,
    )
from django.shortcuts import render, redirect


def get_housings_view(request):
    try:
        if request.method == 'POST':
            form = HousingForm(cities = Cities.by_region(region_id=request.POST.get('region')))
        else:
            form = HousingForm()
        return render(request, 'relocation/main.html', {'form': form})
    except TypeError as e:
        raise e
    return redirect('/')
