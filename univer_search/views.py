from django.shortcuts import render


def uni_search(request):
    return render(request, 'uni_search.html')