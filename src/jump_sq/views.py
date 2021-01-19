from django.shortcuts import render, redirect

from clubs.models import Club


def home(request):
    if Club.objects.all().count() >= 1:
        return render(request, 'home.html')
    else:
        return redirect('/club-registration')
