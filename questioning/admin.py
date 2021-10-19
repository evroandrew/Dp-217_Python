from django.contrib import admin
from .models import TestResult, UserTestResult

admin.site.register(TestResult)
admin.site.register(UserTestResult)
