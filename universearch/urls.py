from django.urls import path
from . import views


urlpatterns = [
    path('', views.uni_search),
]
