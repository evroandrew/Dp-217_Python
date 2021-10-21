from django.http.response import HttpResponse
from .services import (
    CityService as Cities,
    UniversityService as Unies,
    HousingService as Housings
    )
from django.http import JsonResponse, Http404


def get_housings_view(request):
    try:
        return JsonResponse(Housings.get_by_university(Unies.get(**request.GET)))
    except TypeError:
        return Http404()
