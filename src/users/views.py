from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.conf import settings

from .forms import SignUpForm, ProfileForm, UserForm
from clubs.models import Ticket

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    args = {'form': form}
    return render(request, '../templates/registration/signup.html', args)


@login_required
@transaction.atomic
def update_profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        args = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profile.html', args)


class UserJumpsView(ListView):
    model = Ticket
    paginate_by = 20
    template_name = 'user_tickets_list.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object_list = request.user.ticket_set.all().order_by('-flight')
            total_spend = sum([ticket.price for ticket in self.object_list])
            context = super().get_context_data()
            context['total_spend'] = total_spend
            return super().render_to_response(context)
        return redirect(settings.LOGIN_URL)


@login_required
@require_http_methods(["POST"])
def add_ticket_note_view(request, pk):
    if request.method == "POST":
        ticket = Ticket.objects.get(id=pk)
        if request.user == ticket.bought_by:
            notes = request.POST.get('notes')
            ticket.notes = notes
            ticket.save()
    return redirect('user_jumps_list')
