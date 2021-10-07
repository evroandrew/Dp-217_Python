from django.shortcuts import render


def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})
