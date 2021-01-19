from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .forms import ClubForm
from .models import Club


@require_http_methods(["GET", "POST"])
def register_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        if Club.objects.all().count() >= 1:
            return redirect('home')
        else:
            form = ClubForm()
    args = {'form': form}
    return render(request, 'club.html', args)
