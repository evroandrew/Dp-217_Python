from rest_framework import serializers
from .models import QuestionsBase, KlimovCategory


class QuestionsBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsBase
        fields = ['id', 'type', 'question', 'answer_1', 'answer_2', 'result_id_1', 'result_id_2']


class KlimovCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KlimovCategory
        fields = '__all__'
