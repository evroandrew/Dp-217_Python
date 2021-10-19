from django.contrib import admin
from .models import QuestionsBase, KlimovCategory


# class QuestioningAdmin(admin.ModelAdmin):
#     model = TestProfQualification


admin.site.register(QuestionsBase)
admin.site.register(KlimovCategory)
