import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from questioning.models import TestResult
from .services import save_questions_results, create_answer, get_all_answers


def questioning_view(request):
    return render(request, "questioning.html")


@csrf_exempt
def questioning_ajax(request):
    tmp = json.loads(request.read())
    t = loader.get_template('questioning_ajax.html')
    return HttpResponse(t.render(tmp, request))


@csrf_exempt
def questioning_results(request, link=''):
    if request.is_ajax():
        results = json.loads(request.read())['results']
        save_questions_results(request, results)
        resulted_text = create_answer(results)
        return render(request, 'questioning_results.html', resulted_text)
    if link == '':
        title = get_all_answers(request)
    else:
        query = TestResult.objects.filter(url=link)
        if query:
            results = query.first().results
            results = [int(i) for i in results[1:-1].replace(' ', '').split(',')]
            resulted_text = create_answer(results)
            return render(request, 'questioning_results_current.html', resulted_text)
        else:
            title = {'title': 'Результат опитування не знайдено', }
    return render(request, 'questioning_results_full.html', title)
