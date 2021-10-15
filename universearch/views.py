from django.shortcuts import render


def uni_search(request):
    return render(request, 'universearch/search_form.html')
