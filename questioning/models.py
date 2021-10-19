from django.db import models


class QuestionsBase(models.Model):
    type = 1
    question = models.TextField("Запитання", blank=True)
    answer_1 = models.TextField("Відповідь 1", blank=True)
    answer_2 = models.TextField("Відповідь 2", blank=True)
    result_id_1 = models.PositiveSmallIntegerField("Індекс відповіді 1", null=True)
    result_id_2 = models.PositiveSmallIntegerField("Індекс відповіді 2", null=True)

    class Meta:
        verbose_name = "Запитання"
        verbose_name_plural = "Запитання"


class KlimovCategory(models.Model):
    name = models.CharField("Категорія", max_length=20)
    desc = models.TextField("Опис категорії", blank=True)
    professions = models.TextField("Професії", blank=True)

    class Meta:
        verbose_name = "Категорія професії"
        verbose_name_plural = "Категорії професій"
