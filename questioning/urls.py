from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.questioning_view, name='questioning'),
    path('questioning_ajax/', views.questioning_ajax, name='questioning_ajax'),
    re_path('results/', views.questioning_results, name='questioning_results'),
]
