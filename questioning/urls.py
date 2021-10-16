from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.questioning_view, name='questioning'),
    path('ajax/', views.questioning_ajax, name='ajax'),
    path('results/<slug:link>', views.questioning_results),
    path('results/', views.questioning_results, name='questioning_results'),
]
