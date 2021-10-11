import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from questioning.models import TestResult, UserTestResult


def questioning_view(request):
    return render(request, "questioning.html")


@csrf_exempt
def questioning_ajax(request):
    tmp = json.loads(request.read())
    t = loader.get_template('questioning_ajax.html')
    return HttpResponse(t.render(tmp, request))


def save_questions_results(request, results):
    if request.user.is_authenticated:
        test_result = TestResult.objects.create(results=results)
        UserTestResult.objects.create(user_id=request.user.id, result_id=test_result.id)
        return test_result.url
    return 0


@csrf_exempt
def questioning_results(request):
    categories_description = [
        'Сфера діяльності даного типу спрямована на навколишнє нас природу. Це такі професії як ветеринар, еколог, '
        'агроном, геолог, мікробіолог. Професійно важливими якостями даних професій є: інтуїція, емпатія, '
        'вміння піклуватися про кого-небудь крім себе. Такі люди зазвичай трепетно ставляться до представників живої '
        'природи. Для успішної діяльності в професіях цього типу недостатньо просто бути любителем відпочинку на '
        'природі, важливо ще захищати природу, прагнути позитивно взаємодіяти з нею.',
        'Професії даного типу спрямовані на експлуатацію різних технічних пристроїв і приладів, їх обслуговування та '
        'створення. До таких професій належать: металург, водії різного транспорту, пілоти, слюсарі, технологи на '
        'підприємствах, будівельники, автомеханіки і т.д. Для їх успішної діяльності вкрай важливі технічний склад '
        'розуму, уважність, схильність до дій, а не роздумів.',
        "До цього типу належать професії, основний напрямок яких пов'язано зі спілкуванням між людьми і їх взаємний "
        "вплив. Такі як, доктор, викладач, менеджер, учитель, психолог, продавець, тренер. Важливим якістю в даних "
        "професіях є не тільки бажання, але й вміння активної взаємодії з людьми і продуктивного спілкування. Важливо "
        "специфікою при підготовці є добре знання професійної сфери і розвинені комунікативні навички. ",
        "Основним напрямком діяльності даного типу професій є робота з цифрами, формулами, розрахунками, текстами, "
        "базами даних. Це такі професії як програміст, економіст, редактор, аналітик, перекладач, датасайнтіст, "
        "бухгалтер. Професійно важливі якості даного типу професій: точність і аналітичний склад розуму, уважність, "
        "логічне мислення. Для успішної діяльності важливо мати інтерес до різних формулам, таблицям, картам, "
        "схемами, баз даних. ",
        "Професії даного типу підходять людям з розвиненим образним мисленням і творчою жилкою. Фахівці працюють в "
        "напрямку «людина - художній образ», обдаровані талантом або мають покликання до цього з малих років. Їх "
        "діяльність пов'язана з проектуванням, створенням, моделюванням, виготовленням різних творів мистецтва. "
    ]
    professions = [
        "Ландшафтний дизайнер, фотограф, Кінолог, Ветеринар, Агроном, Еколог, Технолог харчової промисловості",
        "Автомеханік, Інженер, Електрик, Пілот",
        "Психологія, SMM-менеджер, Інтернет-маркетолог, Project-менеджер, Маркетинг, Управління.",
        "Data Science, програміст Python, розробка мобільних додатків, інтернет-маркетолог.",
        "Дизайнер, Кліпмейкер, Кіноактор, ТВ - Байєр"]
    professions_options = "Ви можете почати освоювати одну з відповідних вам професій:"
    new_line = '\n'
    results = json.loads(request.read())['results']
    print(save_questions_results(request, results))
    categorised_results = {i: results.count(i) for i in set(results)}
    top_categories = get_top_categories(categorised_results)
    categories = ["природа", "техніка", "людина", "знакова система", "художній образ"]
    expression = ["схильність не виражена", "середньо виражена схильність", "вкрай виражену схильність"]
    expression_id = []
    print(results)
    print(categorised_results)
    print(top_categories)
    for item in top_categories:
        print(categorised_results[item])
    for item in top_categories:
        expression_id.append(categorised_results[item] // 3)
    print(expression_id)
    resulted_text = {'first_description': categories_description[top_categories[0]],
                     'second_description': categories_description[top_categories[1]],
                     'third_description': categories_description[top_categories[2]],
                     'first_professions': f"{professions_options}{new_line}{professions[top_categories[0]]}",
                     'second_professions': f"{professions_options}{new_line}{professions[top_categories[1]]}",
                     'third_professions': f"{professions_options}{new_line}{professions[top_categories[2]]}",
                     'first_result':
                         f"Професії типу «Людина - {categories[top_categories[0]]}» - {expression[expression_id[0]]} ({categorised_results[top_categories[0]]} з 7 балів).",
                     'second_result':
                         f"Професії типу «Людина - {categories[top_categories[1]]}» - {expression[expression_id[1]]} ({categorised_results[top_categories[1]]} з 7 балів).",
                     'third_result':
                         f"Професії типу «Людина - {categories[top_categories[2]]}» - {expression[expression_id[2]]} ({categorised_results[top_categories[2]]} з 7 балів).",
                     }
    t = loader.get_template('questioning_results.html')
    return HttpResponse(t.render(resulted_text, request))


def get_top_categories(resulted_categories):
    resulted_categories_current = resulted_categories.copy()
    max_key = []
    while len(max_key) < 3:
        max_key.append(max(resulted_categories_current, key=resulted_categories_current.get))
        resulted_categories_current[max_key[-1]] = 0
    return max_key
