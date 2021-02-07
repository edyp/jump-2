from django.urls import path

from .views import signup, update_profile_view
from .views import UserJumpsView, add_ticket_note_view

urlpatterns = [
    path('signup', signup, name='signup'),
    path('profile', update_profile_view, name='profile'),
    path('your-jumps', UserJumpsView.as_view(), name='user_jumps_list'),
    path('your-jumps/<int:pk>', add_ticket_note_view, name='add_note')
]
