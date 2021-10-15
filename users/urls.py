from django.urls import path, include
from . import views as users_views


urlpatterns = [
    path('', users_views.profile_view),
    path('', include('django.contrib.auth.urls')),
]
