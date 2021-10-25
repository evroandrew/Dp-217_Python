from django.shortcuts import render, redirect
from .forms import HousingForm


def get_housings_view(request):
    try:
        return render(request, 'relocation/main.html', {'form': HousingForm(request.POST)})
    except TypeError as e:
        raise e
    return redirect('/')
