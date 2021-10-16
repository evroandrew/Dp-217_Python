import datetime
from questioning.models import TestResult


def remove_obsolete_records():
    now = datetime.date.today()
    TestResult.objects.filter(created_date__lt=(now - datetime.timedelta(days=365))).delete()
