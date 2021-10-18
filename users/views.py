import json
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser


PROFESSIONS_MAP = {
    0: {
        'category': 'Людина - природа',
        'examples': "Ландшафтний дизайнер, фотограф, Кінолог, Ветеринар, Агроном, Еколог, Технолог харчової "
                    "промисловості",
        'description': "Сфера діяльності даного типу спрямована на навколишнє нас природу. Це такі професії як "
                       "ветеринар, еколог, агроном, геолог, мікробіолог. Професійно важливими якостями даних професій "
                       "є: інтуїція, емпатія, вміння піклуватися про кого-небудь крім себе. Такі люди зазвичай "
                       "трепетно ставляться до представників живої природи. Для успішної діяльності в професіях цього "
                       "типу недостатньо просто бути любителем відпочинку на природі, важливо ще захищати природу, "
                       "прагнути позитивно взаємодіяти з нею."
    },

    1: {
        'category': 'Людина - техніка',
        'examples': "Автомеханік, Інженер, Електрик, Пілот",
        'description': "Професії даного типу спрямовані на експлуатацію різних технічних пристроїв і приладів, їх "
                       "обслуговування та створення. До таких професій належать: металург, водії різного транспорту, "
                       "пілоти, слюсарі, технологи на підприємствах, будівельники, автомеханіки і т.д. Для їх успішної "
                       "діяльності вкрай важливі технічний склад розуму, уважність, схильність до дій, а не роздумів."
    },

    2: {
        'category': 'Людина - людина',
        'examples': "Психологія, SMM-менеджер, Інтернет-маркетолог, Project-менеджер, Маркетинг, Управління.",
        'description': "До цього типу належать професії, основний напрямок яких пов'язано зі спілкуванням між людьми і "
                       "їх взаємний вплив. Такі як, доктор, викладач, менеджер, учитель, психолог, продавець, тренер. "
                       "Важливим якістю в даних професіях є не тільки бажання, але й вміння активної взаємодії з "
                       "людьми і продуктивного спілкування. Важливо специфікою при підготовці є добре знання "
                       "професійної сфери і розвинені комунікативні навички."
    },

    3: {
        'category': 'Людина - знакова система',
        'examples': "Data Science, програміст Python, розробка мобільних додатків, інтернет-маркетолог.",
        'description': "Основним напрямком діяльності даного типу професій є робота з цифрами, формулами, "
                       "розрахунками, текстами, базами даних. Це такі професії як програміст, економіст, редактор, "
                       "аналітик, перекладач, датасайнтіст, бухгалтер. Професійно важливі якості даного типу професій: "
                       "точність і аналітичний склад розуму, уважність, логічне мислення. Для успішної діяльності "
                       "важливо мати інтерес до різних формулам, таблицям, картам, схемами, баз даних."
    },

    4: {
        'category': 'Людина - художній образ',
        'examples': "Дизайнер, Кліпмейкер, Кіноактор, ТВ - Байєр",
        'description': "Професії даного типу підходять людям з розвиненим образним мисленням і творчою жилкою. Фахівці "
                       "працюють в напрямку «людина - художній образ», обдаровані талантом або мають покликання до "
                       "цього з малих років. Їх діяльність пов'язана з проектуванням, створенням, моделюванням, "
                       "виготовленням різних творів мистецтва."
    },
}


def decode_result(result):
    decoded_result = []
    result_list = json.loads(result)
    for index, data in PROFESSIONS_MAP.items():
        decoded_result.append(
            {
                'profession_info': data,
                'points': result_list.count(index)
            }
        )

    return decoded_result


def profile_view(request):

    user = CustomUser.objects.get(id=request.user.id)
    user_results = [result.result_id.results for result in user.usertestresult_set.all()]

    results = [decode_result(result) for result in user_results]

    for result in results:
        result.sort(key=lambda x: x['points'], reverse=True)
        del result[-(len(result)-3):]

    return render(request, 'users/profile.html', {'user': user, 'results': results})


def registration_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request=request, template_name="registration/registration.html", context={"form": form})
