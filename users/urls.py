from django.urls import path, include
from . import views as users_views


urlpatterns = [
    path('', users_views.profile_view, name='profile'),
    path('', include('django.contrib.auth.urls')),
    path('registration', users_views.registration_view, name='registration'),
    path('edit', users_views.edit_view, name='edit'),
]
