from django.contrib import admin
from .models import TestResult, UserTestResult, QuestionsBase, KlimovCategory

admin.site.register(TestResult)
admin.site.register(UserTestResult)
admin.site.register(QuestionsBase)
admin.site.register(KlimovCategory)
