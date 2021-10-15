from django.db import models
from django.db.models.functions import MD5
from django.core.validators import int_list_validator
from users.models import CustomUser

# if not authorised user
DEFAULT_USER_ID = 0


class TestResult(models.Model):
    """
    Class defining a model, for representing test result with.
    """
    created_date = models.DateTimeField(auto_now_add=True)
    results = models.CharField(validators=[int_list_validator], max_length=20)
    type = 1
    url = MD5([created_date, results, type])


class UserTestResult(models.Model):
    """
    Class defining a model, for representing linked user and test result.
    """
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
    result_id = models.ForeignKey(TestResult, on_delete=models.CASCADE)
