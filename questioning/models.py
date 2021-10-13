from django.db import models


class TestProfQualification(models.Model):
    question = models.TextField(blank=True)
    answer_1 = models.TextField(blank=True)
    answer_2 = models.TextField(blank=True)
    result_id_1 = models.PositiveSmallIntegerField(null=True)
    result_id_2 = models.PositiveSmallIntegerField(null=True)
